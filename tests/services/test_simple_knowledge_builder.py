from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_relation import DocumentaryRelation
from insouwiki.domain.documentary_relation_type import DocumentaryRelationType
from insouwiki.services.simple_knowledge_builder import (
    SimpleKnowledgeBuilder,
)


def test_simple_knowledge_builder_groups_connected_facts():
    fact_1 = DocumentaryFact(
        permanent_id="FACT-00000001",
        author="Jean-Luc Mélenchon",
        statement="Première affirmation documentaire.",
        supporting_sequences=["SEQ-00000001"],
    )

    fact_2 = DocumentaryFact(
        permanent_id="FACT-00000002",
        author="Mathilde Panot",
        statement="Deuxième affirmation documentaire.",
        supporting_sequences=["SEQ-00000002"],
    )

    fact_3 = DocumentaryFact(
        permanent_id="FACT-00000003",
        author="Jean-Luc Mélenchon",
        statement="Troisième affirmation documentaire.",
        supporting_sequences=["SEQ-00000003"],
    )

    relations = [
        DocumentaryRelation(
            permanent_id="REL-00000001",
            relation_type=DocumentaryRelationType.SAME_TOPIC,
            source_fact_id="FACT-00000001",
            target_fact_id="FACT-00000002",
        ),
        DocumentaryRelation(
            permanent_id="REL-00000002",
            relation_type=DocumentaryRelationType.SAME_TOPIC,
            source_fact_id="FACT-00000002",
            target_fact_id="FACT-00000003",
        ),
    ]

    builder = SimpleKnowledgeBuilder()

    knowledge_items = builder.build(
        facts=[fact_1, fact_2, fact_3],
        relations=relations,
    )

    assert len(knowledge_items) == 1

    assert knowledge_items[0].supporting_fact_ids == [
        "FACT-00000001",
        "FACT-00000002",
        "FACT-00000003",
    ]


def test_simple_knowledge_builder_creates_one_knowledge_per_disconnected_group():
    fact_1 = DocumentaryFact(
        permanent_id="FACT-00000001",
        author="Jean-Luc Mélenchon",
        statement="Première affirmation documentaire.",
        supporting_sequences=["SEQ-00000001"],
    )

    fact_2 = DocumentaryFact(
        permanent_id="FACT-00000002",
        author="Mathilde Panot",
        statement="Deuxième affirmation documentaire.",
        supporting_sequences=["SEQ-00000002"],
    )

    builder = SimpleKnowledgeBuilder()

    knowledge_items = builder.build(
        facts=[fact_1, fact_2],
        relations=[],
    )

    assert len(knowledge_items) == 2


def test_simple_knowledge_builder_returns_empty_list_without_facts():
    builder = SimpleKnowledgeBuilder()

    assert builder.build([], []) == []
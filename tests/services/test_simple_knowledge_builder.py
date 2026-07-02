from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_relation import DocumentaryRelation
from insouwiki.domain.documentary_relation_type import DocumentaryRelationType
from insouwiki.services.simple_knowledge_builder import SimpleKnowledgeBuilder


def test_simple_knowledge_builder_groups_facts_by_author():
    fact_1 = DocumentaryFact(
        permanent_id="FACT-00000001",
        author="Jean-Luc Mélenchon",
        statement="Première affirmation documentaire.",
        supporting_sequences=["SEQ-00000001"],
    )

    fact_2 = DocumentaryFact(
        permanent_id="FACT-00000002",
        author="Jean-Luc Mélenchon",
        statement="Deuxième affirmation documentaire.",
        supporting_sequences=["SEQ-00000002"],
    )

    fact_3 = DocumentaryFact(
        permanent_id="FACT-00000003",
        author="Mathilde Panot",
        statement="Troisième affirmation documentaire.",
        supporting_sequences=["SEQ-00000003"],
    )

    relation = DocumentaryRelation(
        permanent_id="REL-00000001",
        relation_type=DocumentaryRelationType.SAME_AUTHOR,
        source_fact_id="FACT-00000001",
        target_fact_id="FACT-00000002",
    )

    builder = SimpleKnowledgeBuilder()

    knowledge_items = builder.build(
        facts=[fact_1, fact_2, fact_3],
        relations=[relation],
    )

    assert len(knowledge_items) == 2

    first = knowledge_items[0]
    second = knowledge_items[1]

    assert first.supporting_fact_ids == [
        "FACT-00000001",
        "FACT-00000002",
    ]

    assert second.supporting_fact_ids == [
        "FACT-00000003",
    ]


def test_simple_knowledge_builder_returns_empty_list_without_facts():
    builder = SimpleKnowledgeBuilder()

    knowledge_items = builder.build(
        facts=[],
        relations=[],
    )

    assert knowledge_items == []
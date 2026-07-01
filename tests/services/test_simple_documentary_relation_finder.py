from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_relation_type import DocumentaryRelationType
from insouwiki.services.simple_documentary_relation_finder import (
    SimpleDocumentaryRelationFinder,
)


def test_simple_documentary_relation_finder_finds_same_author_relation():
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

    finder = SimpleDocumentaryRelationFinder()

    relations = finder.find([fact_1, fact_2])

    assert len(relations) == 1

    relation = relations[0]

    assert relation.permanent_id == "REL-00000001"
    assert relation.relation_type == DocumentaryRelationType.SAME_AUTHOR
    assert relation.source_fact_id == "FACT-00000001"
    assert relation.target_fact_id == "FACT-00000002"


def test_simple_documentary_relation_finder_ignores_different_authors():
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

    finder = SimpleDocumentaryRelationFinder()

    relations = finder.find([fact_1, fact_2])

    assert relations == []
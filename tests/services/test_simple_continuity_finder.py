from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.simple_continuity_finder import (
    SimpleContinuityFinder,
)


def test_detects_documentary_continuity():
    facts = [
        DocumentaryFact(
            permanent_id="FACT-00000001",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000001"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000002",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000002"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000003",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000003"],
        ),
    ]

    finder = SimpleContinuityFinder()

    observations = finder.find(facts)

    assert observations == [
        "Cette affirmation apparaît de manière récurrente dans les sources documentaires disponibles."
    ]
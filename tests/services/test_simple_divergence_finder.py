from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.simple_divergence_finder import (
    SimpleDivergenceFinder,
)


def test_detects_documentary_divergence():
    facts = [
        DocumentaryFact(
            permanent_id="FACT-00000001",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000001"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000002",
            author="Jordan Bardella",
            statement="La retraite doit être à 65 ans.",
            supporting_sequences=["SEQ-00000002"],
        ),
    ]

    finder = SimpleDivergenceFinder()

    observations = finder.find(facts)

    assert observations == [
        "Plusieurs auteurs expriment des affirmations différentes sur ce sujet dans les sources documentaires disponibles."
    ]
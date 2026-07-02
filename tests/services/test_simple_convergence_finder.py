from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.simple_convergence_finder import (
    SimpleConvergenceFinder,
)


def test_detects_documentary_convergence():
    facts = [
        DocumentaryFact(
            permanent_id="FACT-00000001",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000001"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000002",
            author="Mathilde Panot",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000002"],
        ),
    ]

    finder = SimpleConvergenceFinder()

    observations = finder.find(facts)

    assert observations == [
        "Plusieurs auteurs expriment une affirmation similaire sur ce sujet dans les sources documentaires disponibles."
    ]
from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.simple_continuity_finder import (
    SimpleContinuityFinder,
)
from insouwiki.services.simple_convergence_finder import (
    SimpleConvergenceFinder,
)
from insouwiki.services.simple_evolution_finder import (
    SimpleEvolutionFinder,
)


def test_documentary_reasoners_work_together():
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
            statement="La retraite doit être à 65 ans.",
            supporting_sequences=["SEQ-00000003"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000004",
            author="Mathilde Panot",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000004"],
        ),
    ]

    evolution = SimpleEvolutionFinder().find(
        [facts[0], facts[2]]
    )

    continuity = SimpleContinuityFinder().find(
        [facts[0], facts[1], facts[3]]
    )

    convergence = SimpleConvergenceFinder().find(
        [facts[0], facts[3]]
    )

    assert len(evolution) == 1

    assert continuity == [
        "Cette affirmation apparaît de manière récurrente dans les sources documentaires disponibles."
    ]

    assert convergence == [
        "Plusieurs auteurs expriment une affirmation similaire sur ce sujet dans les sources documentaires disponibles."
    ]
from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.exploration_intent import ExplorationIntent
from insouwiki.services.simple_continuity_finder import (
    SimpleContinuityFinder,
)
from insouwiki.services.simple_convergence_finder import (
    SimpleConvergenceFinder,
)
from insouwiki.services.simple_divergence_finder import (
    SimpleDivergenceFinder,
)
from insouwiki.services.simple_evolution_finder import (
    SimpleEvolutionFinder,
)
from insouwiki.services.simple_exploration_builder import (
    SimpleExplorationBuilder,
)
from insouwiki.services.simple_exploration_service import (
    SimpleExplorationService,
)


def test_explore_delegates_to_exploration_builder():
    service = SimpleExplorationService(
        SimpleExplorationBuilder(),
        SimpleContinuityFinder(),
        SimpleEvolutionFinder(),
        SimpleConvergenceFinder(),
        SimpleDivergenceFinder(),
    )

    exploration = service.explore(
        ExplorationIntent.UNDERSTAND,
        "Retraites",
        facts=[],
    )

    assert exploration.intent == ExplorationIntent.UNDERSTAND
    assert exploration.subjects == ["Retraites"]
    assert exploration.observations == []


def test_explore_includes_continuity_observations():
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

    service = SimpleExplorationService(
        SimpleExplorationBuilder(),
        SimpleContinuityFinder(),
        SimpleEvolutionFinder(),
        SimpleConvergenceFinder(),
        SimpleDivergenceFinder(),
    )

    exploration = service.explore(
        ExplorationIntent.UNDERSTAND,
        "Retraites",
        facts=facts,
    )

    assert exploration.observations == [
        "Cette affirmation apparaît de manière récurrente dans les sources documentaires disponibles."
    ]


def test_explore_includes_evolution_observations():
    facts = [
        DocumentaryFact(
            permanent_id="FACT-00000001",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 65 ans.",
            supporting_sequences=["SEQ-00000001"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000002",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000002"],
        ),
    ]

    service = SimpleExplorationService(
        SimpleExplorationBuilder(),
        SimpleContinuityFinder(),
        SimpleEvolutionFinder(),
        SimpleConvergenceFinder(),
        SimpleDivergenceFinder(),
    )

    exploration = service.explore(
        ExplorationIntent.UNDERSTAND,
        "Retraites",
        facts=facts,
    )

    assert exploration.observations == [
        "Une évolution documentaire est observable entre ces faits."
    ]


def test_explore_includes_convergence_observations():
    facts = [
        DocumentaryFact(
            permanent_id="FACT-00000001",
            author="Jean-Luc Mélenchon",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000001"],
        ),
        DocumentaryFact(
            permanent_id="FACT-00000002",
            author="François Ruffin",
            statement="La retraite doit être à 60 ans.",
            supporting_sequences=["SEQ-00000002"],
        ),
    ]

    service = SimpleExplorationService(
        SimpleExplorationBuilder(),
        SimpleContinuityFinder(),
        SimpleEvolutionFinder(),
        SimpleConvergenceFinder(),
        SimpleDivergenceFinder(),
    )

    exploration = service.explore(
        ExplorationIntent.UNDERSTAND,
        "Retraites",
        facts=facts,
    )

    assert exploration.observations == [
        "Plusieurs auteurs expriment une affirmation similaire sur ce sujet dans les sources documentaires disponibles."
    ]


def test_explore_includes_divergence_observations():
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

    service = SimpleExplorationService(
        SimpleExplorationBuilder(),
        SimpleContinuityFinder(),
        SimpleEvolutionFinder(),
        SimpleConvergenceFinder(),
        SimpleDivergenceFinder(),
    )

    exploration = service.explore(
        ExplorationIntent.UNDERSTAND,
        "Retraites",
        facts=facts,
    )

    assert exploration.observations == [
    "Une évolution documentaire est observable entre ces faits.",
    "Plusieurs auteurs expriment des affirmations différentes sur ce sujet dans les sources documentaires disponibles.",
]
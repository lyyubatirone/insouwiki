from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.exploration_intent import ExplorationIntent
from insouwiki.services.simple_continuity_finder import (
    SimpleContinuityFinder,
)
from insouwiki.services.simple_exploration_builder import (
    SimpleExplorationBuilder,
)
from insouwiki.services.simple_exploration_service import (
    SimpleExplorationService,
)


def test_explore_delegates_to_exploration_builder():
    builder = SimpleExplorationBuilder()
    continuity_finder = SimpleContinuityFinder()
    service = SimpleExplorationService(
        builder,
        continuity_finder,
    )

    exploration = service.explore(
        ExplorationIntent.UNDERSTAND,
        "Retraites",
        facts=[],
    )

    assert exploration.intent == ExplorationIntent.UNDERSTAND

    assert exploration.subjects == [
        "Retraites",
    ]

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

    builder = SimpleExplorationBuilder()
    continuity_finder = SimpleContinuityFinder()
    service = SimpleExplorationService(
        builder,
        continuity_finder,
    )

    exploration = service.explore(
        ExplorationIntent.UNDERSTAND,
        "Retraites",
        facts=facts,
    )

    assert exploration.observations == [
        "Cette affirmation apparaît de manière récurrente dans les sources documentaires disponibles."
    ]
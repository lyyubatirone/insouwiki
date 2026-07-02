from insouwiki.domain.exploration_intent import ExplorationIntent
from insouwiki.services.simple_exploration_builder import (
    SimpleExplorationBuilder,
)


def test_build_simple_documentary_exploration():
    builder = SimpleExplorationBuilder()

    exploration = builder.build(
        ExplorationIntent.UNDERSTAND,
        "Retraites",
        observations=[],
    )

    assert exploration.intent == ExplorationIntent.UNDERSTAND

    assert exploration.subjects == [
        "Retraites",
    ]

    assert exploration.observations == []
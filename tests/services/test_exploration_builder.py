from insouwiki.domain.documentary_exploration import DocumentaryExploration
from insouwiki.domain.exploration_intent import ExplorationIntent
from insouwiki.services.exploration_builder import ExplorationBuilder


class FakeExplorationBuilder(ExplorationBuilder):
    def build(
        self,
        intent: ExplorationIntent,
        entry_point: str,
    ) -> DocumentaryExploration:
        return DocumentaryExploration(
            intent=intent,
            subjects=[entry_point],
            observations=[],
        )


def test_build_documentary_exploration():
    builder = FakeExplorationBuilder()

    exploration = builder.build(
        ExplorationIntent.UNDERSTAND,
        "Retraites",
    )

    assert exploration.intent == ExplorationIntent.UNDERSTAND

    assert exploration.subjects == [
        "Retraites",
    ]

    assert exploration.observations == []
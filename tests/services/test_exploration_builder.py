from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)
from insouwiki.services.exploration_builder import (
    ExplorationBuilder,
)


class FakeExplorationBuilder(ExplorationBuilder):
    def build(
        self,
        intent: ExplorationIntent,
        question: DocumentaryQuestion,
        observations: list[str],
    ) -> DocumentaryExploration:
        return DocumentaryExploration(
            intent=intent,
            question=question,
            criteria=(),
            subjects=[
                question.text,
            ],
            observations=observations,
        )


def test_build_documentary_exploration():
    builder = FakeExplorationBuilder()

    question = DocumentaryQuestion(
        text="Retraites",
    )

    exploration = builder.build(
        ExplorationIntent.UNDERSTAND,
        question,
        observations=[],
    )

    assert exploration.intent == ExplorationIntent.UNDERSTAND
    assert exploration.question is question
    assert exploration.subjects == ["Retraites"]
    assert exploration.observations == []
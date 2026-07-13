from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)
from insouwiki.services.simple_exploration_builder import (
    SimpleExplorationBuilder,
)


def test_build_simple_documentary_exploration():
    builder = SimpleExplorationBuilder()

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
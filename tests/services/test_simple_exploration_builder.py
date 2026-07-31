from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)
from insouwiki.services.simple_exploration_builder import (
    SimpleExplorationBuilder,
)
from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.documentary_subject import (
    DocumentarySubject,
)


def test_build_simple_documentary_exploration():
    builder = SimpleExplorationBuilder()

    question = DocumentaryQuestion(
        text="Retraites",
    )

    exploration = builder.build(
        intent=ExplorationIntent.UNDERSTAND,
        question=question,
        subjects=[
            DocumentarySubject(
                permanent_id="SUB-00000001",
                label="Retraites",
            ),
        ],
        criteria=(),
        observations=[],
    )

    assert exploration.intent == ExplorationIntent.UNDERSTAND
    assert exploration.question is question
    assert exploration.subjects == ["Retraites"]
    assert exploration.observations == []

def test_builds_exploration_with_given_subjects_and_criteria():
    builder = SimpleExplorationBuilder()

    question = DocumentaryQuestion(
        text="Que disent les sources sur les retraites ?",
    )

    subjects = [
        DocumentarySubject(
            permanent_id="SUB-00000001",
            label="Retraites",
        ),
    ]

    criteria = (
        DocumentaryCriterion(
            field="expression",
            value="60 ans",
        ),
    )

    exploration = builder.build(
        intent=ExplorationIntent.UNDERSTAND,
        question=question,
        subjects=subjects,
        criteria=criteria,
        observations=[],
    )

    assert exploration.subjects == [
        "Retraites",
    ]
    assert exploration.criteria == criteria
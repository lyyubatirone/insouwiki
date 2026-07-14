from datetime import date

from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)
from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from insouwiki.domain.documentary_date_range import (
    DocumentaryDateRange,
)

def test_create_documentary_exploration():
    question = DocumentaryQuestion(
        text="Que disent les sources sur les retraites ?",
    )

    exploration = DocumentaryExploration(
        intent=ExplorationIntent.UNDERSTAND,
        question=question,
        criteria=(),
        subjects=[
            "Retraites",
        ],
        observations=[
            (
                "Cette affirmation apparaît de manière récurrente "
                "dans les sources documentaires disponibles."
            ),
        ],
    )

    assert exploration.intent == ExplorationIntent.UNDERSTAND
    assert exploration.question is question
    assert exploration.subjects == ["Retraites"]
    assert exploration.observations == [
        (
            "Cette affirmation apparaît de manière récurrente "
            "dans les sources documentaires disponibles."
        ),
    ]

def test_exploration_keeps_documentary_criteria():
    question = DocumentaryQuestion(
        text="Retraite à 60 ans",
    )

    criterion = DocumentaryCriterion(
        field="author",
        value="Jean-Luc Mélenchon",
    )

    exploration = DocumentaryExploration(
        intent=ExplorationIntent.UNDERSTAND,
        question=question,
        subjects=[],
        criteria=(criterion,),
        observations=[],
    )

    assert exploration.criteria == (criterion,)

def test_refine_documentary_exploration():
    question = DocumentaryQuestion(
        text="Retraite à 60 ans",
    )

    exploration = DocumentaryExploration(
        intent=ExplorationIntent.UNDERSTAND,
        question=question,
        criteria=(),
        subjects=[],
        observations=[],
    )

    criterion = DocumentaryCriterion(
        field="auteur",
        value="Jean-Luc Mélenchon",
    )

    refined = exploration.refine(
        criterion,
    )

    assert exploration.criteria == ()

    assert refined.criteria == (
        criterion,
    )

def test_remove_documentary_criterion():
    author_criterion = DocumentaryCriterion(
        field="auteur",
        value="Jean-Luc Mélenchon",
    )

    date_criterion = DocumentaryCriterion(
        field="published_at",
        value=DocumentaryDateRange(
            start=date(2022, 1, 1),
            end=date(2023, 12, 31),
        ),
    )

    exploration = DocumentaryExploration(
        intent=ExplorationIntent.UNDERSTAND,
        question=DocumentaryQuestion(
            text="Retraites",
        ),
        criteria=(),
        subjects=[],
        observations=[],
    )

    exploration = exploration.refine(author_criterion)
    exploration = exploration.refine(date_criterion)

    exploration = exploration.remove(date_criterion)

    assert exploration.criteria == (
        author_criterion,
    )
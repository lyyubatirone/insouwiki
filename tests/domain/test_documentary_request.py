from insouwiki.domain.documentary_criterion import DocumentaryCriterion
from insouwiki.domain.documentary_request import DocumentaryRequest
from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)

def test_documentary_request_contains_the_reader_request():
    request = DocumentaryRequest(
        text="Mélenchon retraites",
    )

    assert request.text == "Mélenchon retraites"


def test_documentary_request_initially_contains_no_criteria():
    request = DocumentaryRequest(
        text="Mélenchon retraites",
    )

    assert request.criteria == ()


def test_documentary_request_contains_documentary_criteria():
    criterion = DocumentaryCriterion(
        field="personality",
        value="Jean-Luc Mélenchon",
    )

    request = DocumentaryRequest(
        text="Mélenchon retraites",
        criteria=(criterion,),
    )

    assert request.criteria == (criterion,)

def test_documentary_request_can_be_refined_with_a_criterion():
    criterion = DocumentaryCriterion(
        field="personality",
        value="Jean-Luc Mélenchon",
    )

    request = DocumentaryRequest(
        text="Mélenchon retraites",
    )

    refined_request = request.refine(criterion)

    assert refined_request.criteria == (criterion,)
    assert request.criteria == ()

def test_documentary_request_can_remove_a_criterion():
    criterion = DocumentaryCriterion(
        field="personality",
        value="Jean-Luc Mélenchon",
    )

    request = DocumentaryRequest(
        text="Mélenchon retraites",
        criteria=(criterion,),
    )

    updated_request = request.remove(criterion)

    assert updated_request.criteria == ()
    assert request.criteria == (criterion,)

def test_documentary_request_can_start_an_exploration():
    request = DocumentaryRequest(
        text="Mélenchon retraites",
    )

    exploration = request.start()

    assert isinstance(
        exploration,
        DocumentaryExploration,
    )

    assert exploration.question.text == (
        "Mélenchon retraites"
    )

    assert exploration.criteria == ()

    assert (
        exploration.intent
        == ExplorationIntent.UNDERSTAND
    )
from insouwiki.consultation.documentary_investigation_view import (
    DocumentaryInvestigationView,
)


def test_documentary_investigation_view_contains_question_and_pieces():
    investigation = DocumentaryInvestigationView(
        question="retraite à 60 ans",
        documentary_pieces=[],
    )

    assert investigation.question == "retraite à 60 ans"

    assert investigation.documentary_pieces == []
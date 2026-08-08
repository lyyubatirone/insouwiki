from insouwiki.web.services.investigation_service import (
    InvestigationService,
)
from insouwiki.web.services.investigation_service import (
    InvestigationService,
)

def test_start_accepts_personality():
    service = InvestigationService()

    state, _ = service.start(
        question="Corse",
        personality="Jean-Luc Mélenchon",
    )

    assert state.question == "Corse"
    assert state.personalities == (
        "Jean-Luc Mélenchon",
    )

def test_start_accepts_multiple_personalities():
    service = InvestigationService()

    state, _ = service.start(
        question="Corse",
        personalities=[
            "Jean-Luc Mélenchon",
            "Manuel Bompard",
        ],
    )

    assert state.question == "Corse"
    assert state.personalities == (
        "Jean-Luc Mélenchon",
        "Manuel Bompard",
    )

def test_ignores_empty_personality():
    service = InvestigationService()

    state, _ = service.start(
        question="retraite à 60 ans",
        personalities=["Manuel Bompard", ""],
    )

    assert state.personalities == (
        "Manuel Bompard",
    )
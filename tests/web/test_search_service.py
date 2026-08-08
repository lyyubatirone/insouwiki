from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.web.services.search_service import (
    SearchService,
)
from datetime import date, timedelta

from insouwiki.domain.documentary_clue import (
    DocumentaryClue,
)
from insouwiki.domain.investigation.investigation_state import (
    InvestigationState,
)

def test_search_service_creates_documentary_question():
    service = SearchService()

    question = service.create_question(
        "retraite à 60 ans",
    )

    assert question == DocumentaryQuestion(
        text="retraite à 60 ans",
    )

def test_search_returns_existing_personality():
    service = SearchService()

    investigation = InvestigationState(
        question="Jean-Luc Mélenchon",
    )

    results = service.search(
        investigation,
    )

    assert len(results) == 1
    assert results[0]["label"] == "Jean-Luc Mélenchon"
    assert results[0]["url"] == (
        "/personnalites/jean-luc-melenchon"
    )
    assert results[0]["kind"] == "Personnalité"

def test_search_returns_documentary_clue():
    service = SearchService()

    investigation = InvestigationState(
        question="retraite à 60 ans",
    )

    results = service.search(
        investigation,
    )

    assert results == [
        DocumentaryClue(
            excerpt="La retraite doit être à 60 ans.",
            speaker="Jean-Luc Mélenchon",
            contexte="France Inter",
            documentary_context="Campagne présidentielle 2022",
            documentary_type="Interview",
            date=date(2022, 4, 12),
            document_id="SRC-00000001",
            sequence_start=timedelta(
                minutes=3,
                seconds=17,
            ),
            sequence_end=timedelta(
                minutes=3,
                seconds=42,
            ),
            source_url=(
                "https://www.youtube.com/watch"
                "?v=WyjX4W0STmM"
            ),
        ),
        DocumentaryClue(
            excerpt=(
                "Nous proposons le retour à la retraite "
                "à 60 ans."
            ),
            speaker="Manuel Bompard",
            contexte="Intervention publique",
            documentary_context="XVIe législature (2022–2024)",
            documentary_type="Discours",
            date=date(2023, 3, 16),
            document_id="SRC-00000001",
            sequence_start=timedelta(
                minutes=1,
                seconds=8,
            ),
            sequence_end=timedelta(
                minutes=1,
                seconds=31,
            ),
            source_url=(
                "https://www.youtube.com/watch"
                "?v=WyjX4W0STmM"
            ),
        ),
    ]

def test_search_filters_by_personality():
    service = SearchService()

    investigation = (
        InvestigationState(
            question="retraite à 60 ans",
        )
        .with_personality(
            "Jean-Luc Mélenchon",
        )
    )

    results = service.search(
        investigation,
    )

    assert results == [
        DocumentaryClue(
            excerpt="La retraite doit être à 60 ans.",
            speaker="Jean-Luc Mélenchon",
            contexte="France Inter",
            documentary_context="Campagne présidentielle 2022",
            documentary_type="Interview",
            date=date(2022, 4, 12),
            document_id="SRC-00000001",
            sequence_start=timedelta(
                minutes=3,
                seconds=17,
            ),
            sequence_end=timedelta(
                minutes=3,
                seconds=42,
            ),
            source_url=(
                "https://www.youtube.com/watch"
                "?v=WyjX4W0STmM"
            ),
        ),
    ]

def test_search_filters_by_context():
    service = SearchService()

    investigation = (
        InvestigationState(
            question="retraite à 60 ans",
        )
        .with_context(
            "Campagne présidentielle 2022",
        )
    )

    results = service.search(
        investigation,
    )

    assert results == [
        DocumentaryClue(
            excerpt="La retraite doit être à 60 ans.",
            speaker="Jean-Luc Mélenchon",
            contexte="France Inter",
            date=date(2022, 4, 12),
            document_id="SRC-00000001",
            documentary_context=(
                "Campagne présidentielle 2022"
            ),
            documentary_type="Interview",
            sequence_start=timedelta(
                minutes=3,
                seconds=17,
            ),
            sequence_end=timedelta(
                minutes=3,
                seconds=42,
            ),
            source_url=(
                "https://www.youtube.com/watch"
                "?v=WyjX4W0STmM"
            ),
        ),
    ]

def test_search_filters_by_document_type():
    service = SearchService()

    investigation = (
        InvestigationState(
            question="retraite à 60 ans",
        )
        .with_document_type(
            "Interview",
        )
    )

    results = service.search(
        investigation,
    )

    assert len(results) == 1
    assert results[0].speaker == "Jean-Luc Mélenchon"
    assert results[0].documentary_type == "Interview"

def test_search_combines_all_documentary_criteria():
    service = SearchService()

    investigation = (
        InvestigationState(
            question="retraite à 60 ans",
        )
        .with_personality(
            "Jean-Luc Mélenchon",
        )
        .with_context(
            "Campagne présidentielle 2022",
        )
        .with_document_type(
            "Interview",
        )
    )

    results = service.search(
        investigation,
    )

    assert len(results) == 1

    assert results[0].speaker == (
        "Jean-Luc Mélenchon"
    )

    assert results[0].documentary_context == (
        "Campagne présidentielle 2022"
    )

    assert results[0].documentary_type == (
        "Interview"
    )
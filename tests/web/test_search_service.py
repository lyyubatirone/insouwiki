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

    results = service.search(
        "Jean-Luc Mélenchon",
    )

    assert len(results) == 1
    assert results[0]["label"] == "Jean-Luc Mélenchon"
    assert results[0]["url"] == (
        "/personnalites/jean-luc-melenchon"
    )
    assert results[0]["kind"] == "Personnalité"

def test_search_returns_documentary_clue():
    service = SearchService()

    results = service.search(
        "retraite à 60 ans",
    )

    assert results == [
        DocumentaryClue(
            excerpt="La retraite doit être à 60 ans.",
            speaker="Jean-Luc Mélenchon",
            contexte="France Inter",
            date=date(2022, 4, 12),
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
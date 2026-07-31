from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.web.services.search_service import (
    SearchService,
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
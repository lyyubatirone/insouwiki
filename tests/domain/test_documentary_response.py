from insouwiki.domain.documentary_clue import DocumentaryClue
from insouwiki.domain.documentary_response import DocumentaryResponse


def test_documentary_response_contains_documentary_clues():
    clue = DocumentaryClue(
        excerpt="La retraite doit être à 60 ans.",
    )

    response = DocumentaryResponse(
        clues=(clue,),
    )

    assert response.clues == (clue,)

def test_documentary_response_can_contain_no_clue():
    response = DocumentaryResponse(
        clues=(),
    )

    assert response.clues == ()

def test_documentary_response_knows_if_it_is_empty():
    response = DocumentaryResponse(
        clues=(),
    )

    assert response.is_empty() is True

def test_documentary_response_knows_if_it_contains_clues():
    clue = DocumentaryClue(
        excerpt="La retraite doit être à 60 ans.",
    )

    response = DocumentaryResponse(
        clues=(clue,),
    )

    assert response.is_empty() is False

def test_empty_documentary_response_invites_to_continue_the_investigation():
    response = DocumentaryResponse(
        clues=(),
    )

    assert response.suggests_continuing_investigation() is True

def test_response_with_clues_does_not_suggest_continuing_investigation():
    clue = DocumentaryClue(
        excerpt="La retraite doit être à 60 ans.",
    )

    response = DocumentaryResponse(
        clues=(clue,),
    )

    assert response.suggests_continuing_investigation() is False

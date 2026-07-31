from insouwiki.domain.documentary_clue import (
    DocumentaryClue,
)
from datetime import date as Date

def test_documentary_clue_contains_the_matching_excerpt():
    clue = DocumentaryClue(
        excerpt=(
            "La retraite doit être à 60 ans "
            "parce que c'est une nécessité."
        ),
    )

    assert clue.excerpt == (
        "La retraite doit être à 60 ans "
        "parce que c'est une nécessité."
    )

def test_documentary_clue_identifies_the_speaker():
    clue = DocumentaryClue(
        excerpt="La retraite doit être à 60 ans.",
        speaker="Jean-Luc Mélenchon",
    )

    assert clue.speaker == "Jean-Luc Mélenchon"

def test_documentary_clue_contains_the_context():
    clue = DocumentaryClue(
        excerpt="La retraite doit être à 60 ans.",
        speaker="Jean-Luc Mélenchon",
        contexte="Invité de France Inter",
    )

    assert clue.contexte == "Invité de France Inter"

from datetime import date


def test_documentary_clue_contains_the_date():
    clue = DocumentaryClue(
        excerpt="La retraite doit être à 60 ans.",
        speaker="Jean-Luc Mélenchon",
        contexte="Invité de France Inter",
        date=date(2022, 4, 12),
    )

    assert clue.date == date(2022, 4, 12)

def test_documentary_clue_contains_other_present_personalities():
    clue = DocumentaryClue(
        excerpt="La retraite doit être à 60 ans.",
        speaker="Jean-Luc Mélenchon",
        contexte="Invité de France Inter",
        date=Date(2022, 4, 12),
        other_personalities=(
            "Léa Salamé",
            "Nicolas Demorand",
        ),
    )

    assert clue.other_personalities == (
        "Léa Salamé",
        "Nicolas Demorand",
    )
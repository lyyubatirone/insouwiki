from insouwiki.domain.documentary_personality import (
    DocumentaryPersonality,
)


def test_documentary_personality_has_identity():
    personality = DocumentaryPersonality(
        permanent_id="PER-00000001",
        slug="jean-luc-melenchon",
        display_name="Jean-Luc Mélenchon",
    )

    assert personality.permanent_id == "PER-00000001"
    assert personality.slug == "jean-luc-melenchon"
    assert personality.display_name == "Jean-Luc Mélenchon"

def test_documentary_personality_keeps_documentary_expressions():
    personality = DocumentaryPersonality(
        permanent_id="PER-00000001",
        slug="jean-luc-melenchon",
        display_name="Jean-Luc Mélenchon",
        documentary_expressions=(
            "Jean-Luc Mélenchon",
            "Mélenchon",
            "JLM",
        ),
    )

    assert personality.documentary_expressions == (
        "Jean-Luc Mélenchon",
        "Mélenchon",
        "JLM",
    )
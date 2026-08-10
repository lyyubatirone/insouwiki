from insouwiki.domain.documentary_theme import (
    DocumentaryTheme,
)


def test_creates_documentary_theme():
    theme = DocumentaryTheme(
        permanent_id="THM-00000001",
        label="Retraites",
        definition=(
            "Prises de parole relatives aux systèmes "
            "de retraite, à leur financement, à l'âge "
            "de départ et aux droits à pension."
        ),
    )

    assert theme.permanent_id == "THM-00000001"
    assert theme.label == "Retraites"
    assert theme.definition == (
        "Prises de parole relatives aux systèmes "
        "de retraite, à leur financement, à l'âge "
        "de départ et aux droits à pension."
    )
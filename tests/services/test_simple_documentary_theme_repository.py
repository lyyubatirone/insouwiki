from insouwiki.domain.documentary_theme import (
    DocumentaryTheme,
)
from insouwiki.services.simple_documentary_theme_repository import (
    SimpleDocumentaryThemeRepository,
)


def test_registers_and_lists_documentary_themes():
    repository = SimpleDocumentaryThemeRepository()

    theme = DocumentaryTheme(
        permanent_id="THM-00000001",
        label="Retraites",
        definition=(
            "Prises de parole relatives aux systèmes "
            "de retraite, à leur financement, à l'âge "
            "de départ et aux droits à pension."
        ),
    )

    repository.register(theme)

    assert repository.list_all() == (theme,)


def test_gets_documentary_theme_by_permanent_id():
    theme = DocumentaryTheme(
        permanent_id="THM-00000001",
        label="Retraites",
    )

    repository = SimpleDocumentaryThemeRepository(
        themes=(theme,),
    )

    assert (
        repository.get_by_permanent_id(
            "THM-00000001",
        )
        == theme
    )


def test_returns_none_for_unknown_documentary_theme():
    repository = SimpleDocumentaryThemeRepository()

    assert (
        repository.get_by_permanent_id(
            "THM-99999999",
        )
        is None
    )
from insouwiki.domain.documentary_theme import (
    DocumentaryTheme,
)
from insouwiki.domain.documentary_theme_repository import (
    DocumentaryThemeRepository,
)


class SimpleDocumentaryThemeRepository(
    DocumentaryThemeRepository,
):
    """
    Référentiel simple des thèmes documentaires.
    """

    def __init__(
        self,
        themes: tuple[DocumentaryTheme, ...] = (),
    ):
        self.themes = themes

    def list_all(
        self,
    ) -> tuple[DocumentaryTheme, ...]:
        return self.themes

    def register(
        self,
        theme: DocumentaryTheme,
    ) -> DocumentaryTheme:
        self.themes = (
            *self.themes,
            theme,
        )

        return theme

    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> DocumentaryTheme | None:
        for theme in self.themes:
            if theme.permanent_id == permanent_id:
                return theme

        return None
from abc import ABC, abstractmethod

from insouwiki.domain.documentary_theme import (
    DocumentaryTheme,
)


class DocumentaryThemeRepository(ABC):
    """
    Référentiel des thèmes documentaires connus par InsouWiki.
    """

    @abstractmethod
    def list_all(
        self,
    ) -> tuple[DocumentaryTheme, ...]:
        raise NotImplementedError

    @abstractmethod
    def register(
        self,
        theme: DocumentaryTheme,
    ) -> DocumentaryTheme:
        raise NotImplementedError

    @abstractmethod
    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> DocumentaryTheme | None:
        raise NotImplementedError
from abc import ABC, abstractmethod

from insouwiki.domain.sequence_theme_association import (
    SequenceThemeAssociation,
)


class SequenceThemeRepository(ABC):
    """
    Référentiel des associations entre
    séquences et thèmes documentaires.
    """

    @abstractmethod
    def register(
        self,
        association: SequenceThemeAssociation,
    ) -> SequenceThemeAssociation:
        raise NotImplementedError

    @abstractmethod
    def find_by_sequence(
        self,
        sequence_id: str,
    ) -> tuple[SequenceThemeAssociation, ...]:
        raise NotImplementedError

    @abstractmethod
    def find_by_theme(
        self,
        theme_id: str,
    ) -> tuple[SequenceThemeAssociation, ...]:
        raise NotImplementedError
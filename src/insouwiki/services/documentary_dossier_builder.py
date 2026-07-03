from abc import ABC, abstractmethod

from insouwiki.domain.documentary_dossier import DocumentaryDossier
from insouwiki.domain.documentary_piece import DocumentaryPiece


class DocumentaryDossierBuilder(ABC):
    """
    Construit un dossier documentaire à partir
    d'un ensemble de pièces documentaires.
    """

    @abstractmethod
    def build(
        self,
        title: str,
        pieces: list[DocumentaryPiece],
    ) -> DocumentaryDossier:
        raise NotImplementedError
from insouwiki.domain.documentary_dossier import DocumentaryDossier
from insouwiki.domain.documentary_piece import DocumentaryPiece
from insouwiki.services.documentary_dossier_builder import (
    DocumentaryDossierBuilder,
)


class SimpleDocumentaryDossierBuilder(DocumentaryDossierBuilder):
    """
    Première implémentation du constructeur
    de dossiers documentaires.
    """

    def build(
        self,
        title: str,
        pieces: list[DocumentaryPiece],
    ) -> DocumentaryDossier:
        return DocumentaryDossier(
            title=title,
            pieces=pieces,
        )
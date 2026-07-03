from insouwiki.domain.documentary_dossier import DocumentaryDossier
from insouwiki.domain.documentary_piece import DocumentaryPiece
from insouwiki.services.documentary_dossier_builder import (
    DocumentaryDossierBuilder,
)


class SimpleDocumentaryDossierBuilder(DocumentaryDossierBuilder):
    """
    Première implémentation du constructeur
    de dossiers documentaires.

    Cette version applique l'ordre documentaire par défaut :
    les pièces sont présentées de la plus récente à la plus ancienne.
    """

    def build(
        self,
        title: str,
        pieces: list[DocumentaryPiece],
    ) -> DocumentaryDossier:
        ordered_pieces = sorted(
            pieces,
            key=lambda piece: piece.published_at,
            reverse=True,
        )

        return DocumentaryDossier(
            title=title,
            pieces=ordered_pieces,
        )
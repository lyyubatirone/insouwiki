from insouwiki.domain.documentary_piece import DocumentaryPiece
from insouwiki.domain.verification_request import VerificationRequest
from insouwiki.services.documentary_index import DocumentaryIndex


class SimpleDocumentaryIndex(DocumentaryIndex):
    """
    Première implémentation de l'index documentaire.

    Cette version retourne l'ensemble des pièces
    documentaires disponibles.
    """

    def __init__(
        self,
        pieces: list[DocumentaryPiece],
    ):
        self._pieces = pieces

    def find(
        self,
        request: VerificationRequest,
    ) -> list[DocumentaryPiece]:
        return self._pieces
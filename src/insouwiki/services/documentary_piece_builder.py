from abc import ABC, abstractmethod

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_piece import DocumentaryPiece
from insouwiki.domain.documentary_sequence import DocumentarySequence


class DocumentaryPieceBuilder(ABC):
    """
    Construit une pièce documentaire à partir d'un document
    et d'une séquence documentaire.
    """

    @abstractmethod
    def build(
        self,
        document: Document,
        sequence: DocumentarySequence,
    ) -> DocumentaryPiece:
        raise NotImplementedError
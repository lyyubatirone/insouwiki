from insouwiki.domain.document import Document
from insouwiki.domain.documentary_piece import DocumentaryPiece
from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.services.documentary_piece_builder import DocumentaryPieceBuilder


class SimpleDocumentaryPieceBuilder(DocumentaryPieceBuilder):
    """
    Construit une pièce documentaire à partir
    d'un document et d'une séquence documentaire.
    """

    def build(
        self,
        document: Document,
        sequence: DocumentarySequence,
    ) -> DocumentaryPiece:
        return DocumentaryPiece(
            permanent_id=sequence.permanent_id,
            author=document.author or "",
            document_title=document.title,
            published_at=document.published_at,
            sequence_text=sequence.text,
            sequence_start=sequence.start,
            sequence_end=sequence.end,
            document_url=document.original_url,
        )
from pydantic import BaseModel
from insouwiki.consultation.documentary_piece_view import DocumentaryPieceView


class DocumentView(BaseModel):
    """
    Vue de consultation d'un document.
    """

    title: str

    author: str | None = None

    original_url: str

    permanent_id: str

    documentary_pieces: list[DocumentaryPieceView] = []
from pydantic import BaseModel

from insouwiki.consultation.documentary_piece_view import (
    DocumentaryPieceView,
)


class DocumentaryInvestigationView(BaseModel):
    """
    Vue de consultation d'une enquête documentaire.
    """

    question: str

    documentary_pieces: list[DocumentaryPieceView]
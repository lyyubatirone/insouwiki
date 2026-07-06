from pydantic import BaseModel


class DocumentaryPieceView(BaseModel):
    """
    Vue de consultation d'une pièce documentaire.
    """

    author: str
    document_title: str
    sequence_text: str
    sequence_start: str
    sequence_end: str
    document_url: str
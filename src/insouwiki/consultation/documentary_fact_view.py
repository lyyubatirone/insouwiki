from pydantic import BaseModel


class DocumentaryFactView(BaseModel):
    """
    Vue de consultation d'un fait documentaire.
    """

    author: str

    statement: str

    source_sequence_id: str

    source_start: str

    source_end: str

    source_url: str
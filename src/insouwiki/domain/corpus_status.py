from pydantic import BaseModel


class CorpusStatus(BaseModel):
    """
    État actuel du patrimoine documentaire.

    Il décrit le corpus documentaire à un instant donné.
    Il ne réalise aucun calcul et ne contient aucune logique.
    """

    sources: int

    documents_discovered: int

    documents_indexed: int

    documents_pending: int

    documents_failed: int
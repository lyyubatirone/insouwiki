from pydantic import BaseModel


class DocumentaryFact(BaseModel):
    """
    Fait documentaire.

    Un fait documentaire décrit une affirmation directement
    observable dans une ou plusieurs séquences documentaires.

    Il ne contient aucune interprétation.
    """

    permanent_id: str

    author: str

    statement: str

    supporting_sequences: list[str]
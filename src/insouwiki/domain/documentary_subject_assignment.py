from pydantic import BaseModel


class DocumentarySubjectAssignment(BaseModel):
    """
    Rattachement d'un sujet documentaire
    à une séquence documentaire.
    """

    permanent_id: str

    subject_id: str

    sequence_id: str
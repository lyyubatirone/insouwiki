from datetime import timedelta

from pydantic import BaseModel


class DocumentarySequence(BaseModel):
    """
    Séquence documentaire horodatée.
    """

    permanent_id: str | None = None

    document_id: str

    start: timedelta

    end: timedelta

    text: str
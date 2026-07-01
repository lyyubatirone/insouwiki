from datetime import timedelta

from pydantic import BaseModel, model_validator


class TranscriptionSegment(BaseModel):
    """
    Segment horodaté produit par un moteur de transcription.

    Il représente une portion continue de la transcription telle
    qu'elle est fournie par le moteur.

    Ce segment n'est pas encore une séquence documentaire.
    """

    start: timedelta
    end: timedelta
    text: str

    @model_validator(mode="after")
    def validate_times(self):
        if self.end < self.start:
            raise ValueError(
                "La fin d'un segment ne peut pas précéder son début."
            )
        return self
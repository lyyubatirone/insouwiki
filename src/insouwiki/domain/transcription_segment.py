from datetime import timedelta

from pydantic import BaseModel, model_validator


class TranscriptionSegment(BaseModel):
    """
    Segment documentaire élémentaire d'une transcription.

    Il représente une portion continue de la transcription
    produite par un moteur de transcription.

    Ce segment constitue l'unité élémentaire d'une transcription.

    Il ne constitue pas encore une séquence documentaire.
    """

    start: timedelta
    end: timedelta
    speaker: str | None = None
    text: str

    @model_validator(mode="after")
    def validate_times(self):
        if self.end < self.start:
            raise ValueError(
                "La fin d'un segment ne peut pas précéder son début."
            )
        return self
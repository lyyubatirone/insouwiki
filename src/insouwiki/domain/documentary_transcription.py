from pydantic import BaseModel

from insouwiki.domain.transcription_segment import (
    TranscriptionSegment,
)


class DocumentaryTranscription(BaseModel):
    """
    Représentation documentaire d'une transcription.

    Une transcription documentaire est associée à un document
    unique et regroupe les segments produits par un moteur de
    transcription.

    Elle ne constitue jamais le document lui-même.

    Le document audiovisuel demeure toujours la référence.
    """

    document_id: str
    language: str
    segments: list[TranscriptionSegment]
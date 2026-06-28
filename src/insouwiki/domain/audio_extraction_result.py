from pathlib import Path

from pydantic import BaseModel


class AudioExtractionResult(BaseModel):
    """
    Résultat d'une extraction audio.
    """

    document_id: str
    audio_path: Path
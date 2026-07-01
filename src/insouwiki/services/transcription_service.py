from pathlib import Path

from insouwiki.domain.document import Document
from insouwiki.domain.transcription import Transcription
from insouwiki.services.transcription_provider import TranscriptionProvider


class TranscriptionService:
    """
    Service d'orchestration de la transcription.

    Il ne transcrit pas lui-même.
    Il délègue la production de la transcription à un provider.
    """

    def __init__(self, provider: TranscriptionProvider):
        self.provider = provider

    def transcribe(
        self,
        document: Document,
        audio_path: Path,
    ) -> Transcription:
        return self.provider.transcribe(
            document=document,
            audio_path=audio_path,
        )
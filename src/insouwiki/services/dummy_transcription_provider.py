from pathlib import Path

from insouwiki.domain.document import Document
from insouwiki.domain.transcription import Transcription
from insouwiki.services.transcription_provider import TranscriptionProvider


class DummyTranscriptionProvider(TranscriptionProvider):
    """
    Provider de transcription factice.

    Il sert uniquement aux tests et à la validation de l'architecture.
    """

    def transcribe(
        self,
        document: Document,
        audio_path: Path,
    ) -> Transcription:
        return Transcription(
            document_id=document.permanent_id or "document:unknown",
            language="fr",
            text=f"Ceci est une transcription de démonstration pour {audio_path.name}.",
            engine="dummy",
        )
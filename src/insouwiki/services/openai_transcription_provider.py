from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from insouwiki.domain.document import Document
from insouwiki.domain.transcription import Transcription
from insouwiki.services.transcription_provider import TranscriptionProvider


class OpenAITranscriptionProvider(TranscriptionProvider):
    """
    Provider de transcription basé sur l'API OpenAI.
    """

    def __init__(self, model: str = "gpt-4o-mini-transcribe"):
        load_dotenv()

        self.model = model
        self.client = OpenAI()

    def transcribe(
        self,
        document: Document,
        audio_path: Path,
    ) -> Transcription:
        with audio_path.open("rb") as audio_file:
            response = self.client.audio.transcriptions.create(
                model=self.model,
                file=audio_file,
                response_format="json",
            )

        return Transcription(
            document_id=document.permanent_id or "document:unknown",
            language="unknown",
            text=response.text,
            engine=f"openai:{self.model}",
        )
import json
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from insouwiki.domain.document import Document
from insouwiki.domain.transcription import Transcription
from insouwiki.domain.transcription_segment import (
    TranscriptionSegment,
)
from insouwiki.services.transcription_provider import (
    TranscriptionProvider,
)


class WhisperTranscriptionProvider(TranscriptionProvider):
    """
    Provider expérimental utilisant whisper-1.

    Il produit une transcription horodatée et conserve
    la réponse complète dans un fichier JSON afin de
    permettre son étude dans EXP-0001.
    """

    def __init__(
        self,
        output_directory: Path = Path("tmp/experiments"),
    ) -> None:
        load_dotenv()

        self._client = OpenAI()
        self._output_directory = output_directory

    def transcribe(
        self,
        document: Document,
        audio_path: Path,
    ) -> Transcription:
        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        with audio_path.open("rb") as audio_file:
            response = self._client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="fr",
                response_format="verbose_json",
                timestamp_granularities=["segment"],
            )

        output_path = (
            self._output_directory
            / "EXP-0001-whisper-response.json"
        )

        response_data = response.model_dump(
            mode="json",
        )

        segments = [
            TranscriptionSegment(
                start=timedelta(
                    seconds=segment["start"],
                ),
                end=timedelta(
                    seconds=segment["end"],
                ),
                text=segment["text"].strip(),
            )
            for segment in response_data.get(
                "segments",
                [],
            )
        ]

        with output_path.open(
            "w",
            encoding="utf-8",
        ) as output_file:
            json.dump(
                response_data,
                output_file,
                ensure_ascii=False,
                indent=2,
            )

        return Transcription(
            document_id=(
                document.permanent_id
                or "document:unknown"
            ),
            language=response.language or "fr",
            text=response.text,
            segments=segments,
            engine="openai:whisper-1",
        )
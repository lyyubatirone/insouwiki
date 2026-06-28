from pathlib import Path

from insouwiki.domain.document import Document
from insouwiki.services.audio_extractor import AudioExtractor


class DummyAudioExtractor(AudioExtractor):
    """
    Extracteur audio factice.

    Il sert uniquement aux tests et à la validation de l'architecture.
    """

    def extract(
        self,
        document: Document,
        output_directory: Path,
    ) -> Path:
        output_directory.mkdir(parents=True, exist_ok=True)

        audio_path = output_directory / "dummy-audio.txt"
        audio_path.write_text(
            f"Audio factice pour {document.permanent_id}",
            encoding="utf-8",
        )

        return audio_path
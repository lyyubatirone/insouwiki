from pathlib import Path

from insouwiki.domain.document import Document
from insouwiki.services.audio_extractor import AudioExtractor


class AudioExtractionService:
    """
    Orchestre l'extraction audio d'un document.

    Le service délègue l'extraction à un AudioExtractor
    et ne connaît pas son implémentation concrète.
    """

    def __init__(self, extractor: AudioExtractor):
        self._extractor = extractor

    def extract(
        self,
        document: Document,
        output_directory: Path,
    ) -> Path:
        return self._extractor.extract(
            document=document,
            output_directory=output_directory,
        )
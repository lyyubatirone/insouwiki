from pathlib import Path

from insouwiki.domain.audio_extraction_result import AudioExtractionResult
from insouwiki.domain.document import Document
from insouwiki.services.audio_extractor import AudioExtractor


class AudioExtractionService:
    """
    Orchestre l'extraction audio d'un document.

    Le service délègue l'extraction à un AudioExtractor
    et retourne un résultat métier.
    """

    def __init__(self, extractor: AudioExtractor):
        self._extractor = extractor

    def extract(
        self,
        document: Document,
        output_directory: Path,
    ) -> AudioExtractionResult:
        audio_path = self._extractor.extract(
            document=document,
            output_directory=output_directory,
        )

        return AudioExtractionResult(
            document_id=document.permanent_id or "document:unknown",
            audio_path=audio_path,
        )
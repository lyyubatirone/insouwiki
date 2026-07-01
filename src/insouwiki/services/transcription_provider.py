from abc import ABC, abstractmethod
from pathlib import Path

from insouwiki.domain.document import Document
from insouwiki.domain.transcription import Transcription


class TranscriptionProvider(ABC):
    """
    Contrat des moteurs de transcription.

    Un provider produit une transcription
    à partir d'un document et d'un fichier audio.
    """

    @abstractmethod
    def transcribe(
        self,
        document: Document,
        audio_path: Path,
    ) -> Transcription:
        """
        Produit une transcription.
        """
        ...
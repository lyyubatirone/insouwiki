from abc import ABC, abstractmethod

from insouwiki.domain.document import Document
from insouwiki.domain.transcription import Transcription


class TranscriptionProvider(ABC):
    """
    Contrat des moteurs de transcription.

    Un provider sait produire une transcription
    à partir d'un document.
    """

    @abstractmethod
    def transcribe(self, document: Document) -> Transcription:
        """
        Produit une transcription du document.
        """
        ...
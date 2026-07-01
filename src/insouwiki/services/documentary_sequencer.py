from abc import ABC, abstractmethod

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.domain.transcription import Transcription


class DocumentarySequencer(ABC):
    """
    Transforme une transcription en séquences documentaires.
    """

    @abstractmethod
    def sequence(
        self,
        document: Document,
        transcription: Transcription,
    ) -> list[DocumentarySequence]:
        ...
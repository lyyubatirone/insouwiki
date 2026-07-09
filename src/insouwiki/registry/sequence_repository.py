from abc import ABC, abstractmethod

from insouwiki.domain.documentary_sequence import DocumentarySequence


class DocumentarySequenceRepository(ABC):
    """
    Stockage des séquences documentaires.
    """

    @abstractmethod
    def register_many(
        self,
        sequences: list[DocumentarySequence],
    ) -> None:
        ...

    @abstractmethod
    def find_by_document(
        self,
        document_id: str,
    ) -> list[DocumentarySequence]:
        ...
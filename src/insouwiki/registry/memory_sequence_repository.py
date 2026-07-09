from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.registry.sequence_repository import DocumentarySequenceRepository


class MemoryDocumentarySequenceRepository(DocumentarySequenceRepository):

    def __init__(self):
        self._sequences: list[DocumentarySequence] = []

    def register_many(
        self,
        sequences: list[DocumentarySequence],
    ) -> None:
        self._sequences.extend(sequences)

    def find_by_document(
        self,
        document_id: str,
    ) -> list[DocumentarySequence]:
        return [
            sequence
            for sequence in self._sequences
            if sequence.document_id == document_id
        ]
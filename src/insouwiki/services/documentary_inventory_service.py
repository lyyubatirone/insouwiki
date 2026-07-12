from insouwiki.domain.documentary_inventory import (
    DocumentaryInventory,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.registry.repository import DocumentRepository
from insouwiki.registry.sequence_repository import (
    DocumentarySequenceRepository,
)


class DocumentaryInventoryService:
    """
    Établit un inventaire documentaire à partir
    d'une question formulée par le lecteur.
    """

    def __init__(
        self,
        document_repository: DocumentRepository,
        sequence_repository: DocumentarySequenceRepository,
    ) -> None:
        self._document_repository = document_repository
        self._sequence_repository = sequence_repository

    def build(
        self,
        question: DocumentaryQuestion,
    ) -> DocumentaryInventory:
        sequences = self._sequence_repository.search(
            question.text,
        )

        documents = []
        seen_document_ids: set[str] = set()

        for sequence in sequences:
            if sequence.document_id in seen_document_ids:
                continue

            document = self._document_repository.get_by_permanent_id(
                sequence.document_id,
            )

            if document is None:
                continue

            seen_document_ids.add(sequence.document_id)
            documents.append(document)

        return DocumentaryInventory(
            documents=tuple(documents),
        )
from insouwiki.domain.documentary_processing_batch import (
    DocumentaryProcessingBatch,
)
from insouwiki.registry.repository import DocumentRepository
from insouwiki.services.document_indexer import (
    DocumentIndexer,
)


class DocumentaryProcessingBatchProcessor:
    def __init__(
        self,
        repository: DocumentRepository,
        indexer: DocumentIndexer,
    ) -> None:
        self.repository = repository
        self.indexer = indexer

    def process(
        self,
        batch: DocumentaryProcessingBatch,
    ) -> None:
        if batch.status != "approved":
            raise ValueError(
                "Only an approved batch can be processed."
            )

        for document_id in batch.document_ids:
            document = self.repository.get_by_permanent_id(
                document_id,
            )

            if document is None:
                raise ValueError(
                    f"Unknown document: {document_id}"
                )

            self.indexer.index(
                document,
            )
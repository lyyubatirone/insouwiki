from insouwiki.domain.document import Document
from insouwiki.registry.repository import DocumentRepository
from insouwiki.services.documentary_processing_batch_builder import (
    DocumentaryProcessingBatchBuilder,
)


class DocumentaryProcessingBatchPreparer:
    def __init__(
        self,
        repository: DocumentRepository,
        builder: DocumentaryProcessingBatchBuilder | None = None,
    ) -> None:
        self.repository = repository
        self.builder = (
            builder
            if builder is not None
            else DocumentaryProcessingBatchBuilder()
        )

    def prepare(
        self,
        name: str,
        document_ids: list[str],
    ):
        documents: list[Document] = []

        for document_id in document_ids:
            document = self.repository.get_by_permanent_id(
                document_id,
            )

            if document is None:
                raise ValueError(
                    f"Unknown document: {document_id}"
                )

            documents.append(
                document,
            )

        return self.builder.build(
            name=name,
            documents=documents,
        )
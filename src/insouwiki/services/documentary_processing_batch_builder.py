from insouwiki.domain.document import Document
from insouwiki.domain.documentary_processing_batch import (
    DocumentaryProcessingBatch,
)


class DocumentaryProcessingBatchBuilder:
    def build(
        self,
        name: str,
        documents: list[Document],
    ) -> DocumentaryProcessingBatch:
        for document in documents:
            if (
                document.permanent_id is not None
                and document.duration is None
            ):
                raise ValueError(
                    "Cannot build a processing batch "
                    "with a document whose duration "
                    "is unknown."
                )

        return DocumentaryProcessingBatch(
            name=name,
            document_ids=[
                document.permanent_id
                for document in documents
                if document.permanent_id is not None
            ],
            document_durations=[
                document.duration
                for document in documents
                if (
                    document.permanent_id is not None
                    and document.duration is not None
                )
            ],
        )
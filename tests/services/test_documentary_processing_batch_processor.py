from datetime import timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_processing_batch import (
    DocumentaryProcessingBatch,
)
from insouwiki.domain.enums import DocumentKind
from insouwiki.services.documentary_processing_batch_processor import (
    DocumentaryProcessingBatchProcessor,
)


class FakeDocumentRepository:
    def __init__(
        self,
        documents: list[Document],
    ):
        self.documents = {
            document.permanent_id: document
            for document in documents
        }

    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> Document | None:
        return self.documents.get(
            permanent_id
        )


class FakeDocumentIndexer:
    def __init__(self):
        self.indexed_documents: list[Document] = []

    def index(
        self,
        document: Document,
    ) -> None:
        self.indexed_documents.append(
            document
        )


def test_processes_every_document_of_approved_batch():
    documents = [
        Document(
            permanent_id="SRC-00000001",
            origin_key="youtube:one",
            document_kind=DocumentKind.VIDEO,
            title="Document 1",
            original_url="https://example.com/one",
            duration=timedelta(minutes=30),
        ),
        Document(
            permanent_id="SRC-00000002",
            origin_key="youtube:two",
            document_kind=DocumentKind.VIDEO,
            title="Document 2",
            original_url="https://example.com/two",
            duration=timedelta(minutes=45),
        ),
    ]

    repository = FakeDocumentRepository(
        documents,
    )

    indexer = FakeDocumentIndexer()

    processor = DocumentaryProcessingBatchProcessor(
        repository=repository,
        indexer=indexer,
    )

    batch = DocumentaryProcessingBatch(
        permanent_id="BATCH-00000001",
        name="Retraites",
        document_ids=[
            "SRC-00000001",
            "SRC-00000002",
        ],
        document_durations=[
            timedelta(minutes=30),
            timedelta(minutes=45),
        ],
        status="approved",
    )

    processor.process(
        batch,
    )

    assert indexer.indexed_documents == documents

import pytest


def test_refuses_unapproved_batch_before_indexing():
    document = Document(
        permanent_id="SRC-00000001",
        origin_key="youtube:one",
        document_kind=DocumentKind.VIDEO,
        title="Document 1",
        original_url="https://example.com/one",
        duration=timedelta(minutes=30),
    )

    repository = FakeDocumentRepository(
        [document],
    )

    indexer = FakeDocumentIndexer()

    processor = DocumentaryProcessingBatchProcessor(
        repository=repository,
        indexer=indexer,
    )

    batch = DocumentaryProcessingBatch(
        permanent_id="BATCH-00000002",
        name="Lot non approuvé",
        document_ids=[
            "SRC-00000001",
        ],
        document_durations=[
            timedelta(minutes=30),
        ],
        status="prepared",
    )

    with pytest.raises(ValueError):
        processor.process(
            batch,
        )

    assert indexer.indexed_documents == []

def test_stops_when_batch_contains_unknown_document():
    first_document = Document(
        permanent_id="SRC-00000001",
        origin_key="youtube:one",
        document_kind=DocumentKind.VIDEO,
        title="Document 1",
        original_url="https://example.com/one",
        duration=timedelta(minutes=30),
    )

    repository = FakeDocumentRepository(
        [first_document],
    )

    indexer = FakeDocumentIndexer()

    processor = DocumentaryProcessingBatchProcessor(
        repository=repository,
        indexer=indexer,
    )

    batch = DocumentaryProcessingBatch(
        permanent_id="BATCH-00000003",
        name="Lot incomplet",
        document_ids=[
            "SRC-00000001",
            "SRC-99999999",
            "SRC-00000003",
        ],
        document_durations=[
            timedelta(minutes=30),
            timedelta(minutes=20),
            timedelta(minutes=10),
        ],
        status="approved",
    )

    with pytest.raises(
        ValueError,
        match="Unknown document: SRC-99999999",
    ):
        processor.process(
            batch,
        )

    assert indexer.indexed_documents == [
        first_document,
    ]

def test_stops_when_document_indexing_fails():
    documents = [
        Document(
            permanent_id="SRC-00000001",
            origin_key="youtube:one",
            document_kind=DocumentKind.VIDEO,
            title="Document 1",
            original_url="https://example.com/one",
            duration=timedelta(minutes=30),
        ),
        Document(
            permanent_id="SRC-00000002",
            origin_key="youtube:two",
            document_kind=DocumentKind.VIDEO,
            title="Document 2",
            original_url="https://example.com/two",
            duration=timedelta(minutes=20),
        ),
        Document(
            permanent_id="SRC-00000003",
            origin_key="youtube:three",
            document_kind=DocumentKind.VIDEO,
            title="Document 3",
            original_url="https://example.com/three",
            duration=timedelta(minutes=10),
        ),
    ]

    repository = FakeDocumentRepository(
        documents,
    )

    class FailingDocumentIndexer:
        def __init__(self):
            self.attempted_documents = []

        def index(
            self,
            document,
        ):
            self.attempted_documents.append(
                document,
            )

            if (
                document.permanent_id
                == "SRC-00000002"
            ):
                raise RuntimeError(
                    "Indexing failed"
                )

    indexer = FailingDocumentIndexer()

    processor = DocumentaryProcessingBatchProcessor(
        repository=repository,
        indexer=indexer,
    )

    batch = DocumentaryProcessingBatch(
        permanent_id="BATCH-00000004",
        name="Lot avec erreur",
        document_ids=[
            "SRC-00000001",
            "SRC-00000002",
            "SRC-00000003",
        ],
        document_durations=[
            timedelta(minutes=30),
            timedelta(minutes=20),
            timedelta(minutes=10),
        ],
        status="approved",
    )

    with pytest.raises(
        RuntimeError,
        match="Indexing failed",
    ):
        processor.process(
            batch,
        )

    assert indexer.attempted_documents == [
        documents[0],
        documents[1],
    ]
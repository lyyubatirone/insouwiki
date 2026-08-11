from datetime import timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.enums import DocumentKind
from insouwiki.services.documentary_processing_batch_preparer import (
    DocumentaryProcessingBatchPreparer,
)


class FakeDocumentRepository:
    def __init__(
        self,
        documents: list[Document],
    ) -> None:
        self.documents = {
            document.permanent_id: document
            for document in documents
        }

    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> Document | None:
        return self.documents.get(
            permanent_id,
        )


def test_prepares_batch_from_document_ids():
    repository = FakeDocumentRepository(
        [
            Document(
                permanent_id="SRC-00000001",
                origin_key="youtube:one",
                document_kind=DocumentKind.VIDEO,
                title="Document 1",
                original_url="https://example.com/one",
                duration=timedelta(hours=1),
            ),
            Document(
                permanent_id="SRC-00000002",
                origin_key="youtube:two",
                document_kind=DocumentKind.VIDEO,
                title="Document 2",
                original_url="https://example.com/two",
                duration=timedelta(minutes=30),
            ),
        ]
    )

    preparer = DocumentaryProcessingBatchPreparer(
        repository=repository,
    )

    batch = preparer.prepare(
        name="Retraites",
        document_ids=[
            "SRC-00000001",
            "SRC-00000002",
        ],
    )

    assert batch.name == "Retraites"

    assert batch.document_ids == [
        "SRC-00000001",
        "SRC-00000002",
    ]

    assert batch.document_count == 2

    assert batch.total_duration == timedelta(
        hours=1,
        minutes=30,
    )

    assert batch.status == "prepared"

import pytest


def test_refuses_unknown_document_id():
    repository = FakeDocumentRepository(
        [
            Document(
                permanent_id="SRC-00000001",
                origin_key="youtube:one",
                document_kind=DocumentKind.VIDEO,
                title="Document 1",
                original_url="https://example.com/one",
                duration=timedelta(hours=1),
            ),
        ]
    )

    preparer = DocumentaryProcessingBatchPreparer(
        repository=repository,
    )

    with pytest.raises(ValueError):
        preparer.prepare(
            name="Retraites",
            document_ids=[
                "SRC-00000001",
                "SRC-99999999",
            ],
        )
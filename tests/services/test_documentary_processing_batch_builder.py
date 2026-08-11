from datetime import timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_processing_batch import (
    DocumentaryProcessingBatch,
)
from insouwiki.domain.enums import DocumentKind
from insouwiki.services.documentary_processing_batch_builder import (
    DocumentaryProcessingBatchBuilder,
)


def test_builds_processing_batch_from_documents():
    documents = [
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

    builder = DocumentaryProcessingBatchBuilder()

    batch = builder.build(
        name="Retraites",
        documents=documents,
    )

    assert batch == DocumentaryProcessingBatch(
        name="Retraites",
        document_ids=[
            "SRC-00000001",
            "SRC-00000002",
        ],
        document_durations=[
            timedelta(hours=1),
            timedelta(minutes=30),
        ],
    )

import pytest

def test_refuses_document_without_known_duration():
    documents = [
        Document(
            permanent_id="SRC-00000001",
            origin_key="youtube:unknown-duration",
            document_kind=DocumentKind.VIDEO,
            title="Document sans durée",
            original_url="https://example.com/unknown-duration",
            duration=None,
        ),
    ]

    builder = DocumentaryProcessingBatchBuilder()

    with pytest.raises(ValueError):
        builder.build(
            name="Retraites",
            documents=documents,
        )
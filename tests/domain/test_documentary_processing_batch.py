from datetime import timedelta

from insouwiki.domain.documentary_processing_batch import (
    DocumentaryProcessingBatch,
)


def test_documentary_processing_batch_has_total_duration():
    batch = DocumentaryProcessingBatch(
        name="Retraites",
        document_ids=[
            "SRC-00000001",
            "SRC-00000002",
            "SRC-00000003",
        ],
        document_durations=[
            timedelta(hours=1),
            timedelta(minutes=30),
            timedelta(minutes=45),
        ],
    )

    assert batch.document_count == 3

    assert batch.total_duration == timedelta(
        hours=2,
        minutes=15,
    )

def test_prepared_batch_can_be_approved():
    batch = DocumentaryProcessingBatch(
        name="Retraites",
        document_ids=[
            "SRC-00000001",
        ],
        document_durations=[
            timedelta(hours=1),
        ],
    )

    assert batch.status == "prepared"

    approved_batch = batch.approve()

    assert approved_batch.status == "approved"

import pytest


def test_only_approved_batch_can_be_processed():
    batch = DocumentaryProcessingBatch(
        name="Retraites",
        document_ids=[
            "SRC-00000001",
        ],
        document_durations=[
            timedelta(hours=1),
        ],
    )

    with pytest.raises(ValueError):
        batch.mark_processed()

    approved_batch = batch.approve()

    processed_batch = approved_batch.mark_processed()

    assert processed_batch.status == "processed"

def test_processing_batch_can_have_permanent_id():
    batch = DocumentaryProcessingBatch(
        permanent_id="BATCH-00000001",
        name="Retraites",
        document_ids=[
            "SRC-00000001",
        ],
        document_durations=[
            timedelta(hours=1),
        ],
    )

    assert batch.permanent_id == "BATCH-00000001"
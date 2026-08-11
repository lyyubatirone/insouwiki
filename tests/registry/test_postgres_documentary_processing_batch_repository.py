from datetime import timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_processing_batch import (
    DocumentaryProcessingBatch,
)
from insouwiki.domain.enums import DocumentKind
from insouwiki.registry.postgres import (
    PostgresDocumentRepository,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
)
from insouwiki.registry.postgres_documentary_processing_batch_repository import (
    PostgresDocumentaryProcessingBatchRepository,
)


def cleanup_test_document(
    origin_key: str,
) -> None:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT DISTINCT
                    batch_documents.batch_id
                FROM documentary_processing_batch_documents
                    AS batch_documents
                JOIN documents
                    ON documents.permanent_id
                    = batch_documents.document_id
                WHERE documents.origin_key = %s
                """,
                (origin_key,),
            )

            batch_ids = [
                row[0]
                for row in cur.fetchall()
            ]

            cur.execute(
                """
                DELETE FROM documentary_processing_batch_documents
                WHERE document_id IN (
                    SELECT permanent_id
                    FROM documents
                    WHERE origin_key = %s
                )
                """,
                (origin_key,),
            )

            for batch_id in batch_ids:
                cur.execute(
                    """
                    DELETE FROM documentary_processing_batches
                    WHERE permanent_id = %s
                    """,
                    (batch_id,),
                )

            cur.execute(
                """
                DELETE FROM documents
                WHERE origin_key = %s
                """,
                (origin_key,),
            )

        conn.commit()


def test_registers_and_reads_processing_batch():
    origin_key = "test:processing-batch-document"

    cleanup_test_document(
        origin_key,
    )

    document_repository = PostgresDocumentRepository()

    document = Document(
        origin_key=origin_key,
        document_kind=DocumentKind.VIDEO,
        title="Document du lot",
        original_url="https://example.com/batch-document",
        duration=timedelta(minutes=30),
    )

    registration = document_repository.register(
        document,
    )

    repository = (
        PostgresDocumentaryProcessingBatchRepository()
    )

    batch = DocumentaryProcessingBatch(
        permanent_id=None,
        name="Retraites",
        document_ids=[
            registration.document_id,
        ],
        document_durations=[
            timedelta(minutes=30),
        ],
    )

    stored_batch = repository.register(
        batch,
    )

    assert stored_batch.permanent_id is not None

    assert stored_batch.permanent_id.startswith(
        "BATCH-"
    )

    reloaded = repository.get_by_permanent_id(
        stored_batch.permanent_id,
    )

    assert reloaded is not None
    assert reloaded.name == "Retraites"
    assert reloaded.status == "prepared"

    assert reloaded.document_ids == [
        registration.document_id,
    ]

    assert reloaded.total_duration == timedelta(
        minutes=30,
    )

    cleanup_test_document(
        origin_key,
    )


def test_updates_processing_batch_status():
    origin_key = (
        "test:processing-batch-status-document"
    )

    cleanup_test_document(
        origin_key,
    )

    document_repository = PostgresDocumentRepository()

    document = Document(
        origin_key=origin_key,
        document_kind=DocumentKind.VIDEO,
        title="Document du lot",
        original_url=(
            "https://example.com/"
            "batch-status-document"
        ),
        duration=timedelta(minutes=30),
    )

    registration = document_repository.register(
        document,
    )

    repository = (
        PostgresDocumentaryProcessingBatchRepository()
    )

    batch = DocumentaryProcessingBatch(
        name="Retraites",
        document_ids=[
            registration.document_id,
        ],
        document_durations=[
            timedelta(minutes=30),
        ],
    )

    stored_batch = repository.register(
        batch,
    )

    approved_batch = stored_batch.approve()

    repository.update_status(
        approved_batch,
    )

    reloaded = repository.get_by_permanent_id(
        stored_batch.permanent_id,
    )

    assert reloaded is not None

    assert reloaded.permanent_id == (
        stored_batch.permanent_id
    )

    assert reloaded.status == "approved"

    cleanup_test_document(
        origin_key,
    )

def test_updates_processing_batch_status_to_processed():
    origin_key = (
        "test:processing-batch-processed-document"
    )

    cleanup_test_document(
        origin_key,
    )

    document_repository = PostgresDocumentRepository()

    document = Document(
        origin_key=origin_key,
        document_kind=DocumentKind.VIDEO,
        title="Document du lot traité",
        original_url=(
            "https://example.com/"
            "batch-processed-document"
        ),
        duration=timedelta(minutes=30),
    )

    registration = document_repository.register(
        document,
    )

    repository = (
        PostgresDocumentaryProcessingBatchRepository()
    )

    batch = DocumentaryProcessingBatch(
        name="Retraites",
        document_ids=[
            registration.document_id,
        ],
        document_durations=[
            timedelta(minutes=30),
        ],
    )

    stored_batch = repository.register(
        batch,
    )

    approved_batch = stored_batch.approve()

    repository.update_status(
        approved_batch,
    )

    processed_batch = (
        approved_batch.mark_processed()
    )

    repository.update_status(
        processed_batch,
    )

    reloaded = repository.get_by_permanent_id(
        stored_batch.permanent_id,
    )

    assert reloaded is not None

    assert reloaded.permanent_id == (
        stored_batch.permanent_id
    )

    assert reloaded.status == "processed"

    cleanup_test_document(
        origin_key,
    )
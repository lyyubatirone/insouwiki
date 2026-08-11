from datetime import timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.enums import DocumentKind
from insouwiki.registry.postgres import (
    PostgresDocumentRepository,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
)


def test_postgres_document_repository_persists_duration():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documents
                WHERE origin_key = %s
                """,
                ("test:document-duration",),
            )

        conn.commit()

    repository = PostgresDocumentRepository()

    document = Document(
        origin_key="test:document-duration",
        document_kind=DocumentKind.VIDEO,
        title="Document avec durée",
        original_url=(
            "https://example.com/document-duration"
        ),
        duration=timedelta(
            minutes=42,
            seconds=15,
        ),
    )

    result = repository.register(document)

    stored = repository.get_by_permanent_id(
        result.document_id,
    )

    assert stored is not None
    assert stored.duration == timedelta(
        minutes=42,
        seconds=15,
    )

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documents
                WHERE origin_key = %s
                """,
                ("test:document-duration",),
            )

        conn.commit()

def test_postgres_document_repository_updates_duration_of_existing_document():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documents
                WHERE origin_key = %s
                """,
                ("test:existing-document-duration",),
            )

        conn.commit()

    repository = PostgresDocumentRepository()

    discovered_document = Document(
        origin_key="test:existing-document-duration",
        document_kind=DocumentKind.VIDEO,
        title="Document existant",
        original_url=(
            "https://example.com/existing-document"
        ),
        duration=None,
    )

    first_registration = repository.register(
        discovered_document,
    )

    enriched_document = Document(
        origin_key="test:existing-document-duration",
        document_kind=DocumentKind.VIDEO,
        title="Document existant",
        original_url=(
            "https://example.com/existing-document"
        ),
        duration=timedelta(
            minutes=42,
            seconds=15,
        ),
    )

    second_registration = repository.register(
        enriched_document,
    )

    stored = repository.get_by_permanent_id(
        first_registration.document_id,
    )

    assert second_registration.created is False

    assert (
        second_registration.document_id
        == first_registration.document_id
    )

    assert stored is not None

    assert stored.duration == timedelta(
        minutes=42,
        seconds=15,
    )

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documents
                WHERE origin_key = %s
                """,
                ("test:existing-document-duration",),
            )

        conn.commit()
from datetime import timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.enums import DocumentKind


def test_document_can_have_duration():
    document = Document(
        origin_key="youtube:test-video",
        document_kind=DocumentKind.VIDEO,
        title="Document de test",
        original_url="https://www.youtube.com/watch?v=test",
        duration=timedelta(
            minutes=42,
            seconds=15,
        ),
    )

    assert document.duration == timedelta(
        minutes=42,
        seconds=15,
    )
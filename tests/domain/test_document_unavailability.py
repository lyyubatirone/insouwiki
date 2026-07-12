from insouwiki.domain.document import Document
from insouwiki.domain.enums import (
    DocumentKind,
    ProcessingStatus,
)


def test_document_can_become_unavailable():
    document = Document(
        origin_key="youtube:abc123",
        document_kind=DocumentKind.VIDEO,
        title="Une vidéo",
        original_url="https://www.youtube.com/watch?v=abc123",
    )

    assert document.status == ProcessingStatus.DISCOVERED

    document.status = ProcessingStatus.UNAVAILABLE

    assert document.status == ProcessingStatus.UNAVAILABLE
from datetime import datetime, timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.domain.enums import DocumentKind
from insouwiki.services.youtube_timestamp_link_builder import (
    YouTubeTimestampLinkBuilder,
)


def test_builds_youtube_timestamp_link():
    document = Document(
        permanent_id="DOC-00000001",
        origin_key="youtube:video:abc123",
        document_kind=DocumentKind.VIDEO,
        title="Discours de test",
        original_url="https://www.youtube.com/watch?v=abc123",
        author="Jean Dupont",
        published_at=datetime(2026, 1, 1),
    )

    sequence = DocumentarySequence(
        permanent_id="SEQ-00000001",
        document_id="DOC-00000001",
        start=timedelta(seconds=123),
        end=timedelta(seconds=150),
        text="Texte de la séquence.",
    )

    builder = YouTubeTimestampLinkBuilder()

    assert builder.build(document, sequence) == (
        "https://www.youtube.com/watch?v=abc123&t=123s"
    )
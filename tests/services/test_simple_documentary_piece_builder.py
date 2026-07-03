from datetime import datetime, timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.domain.enums import DocumentKind
from insouwiki.services.simple_documentary_piece_builder import (
    SimpleDocumentaryPieceBuilder,
)


def test_build_documentary_piece():
    builder = SimpleDocumentaryPieceBuilder()

    document = Document(
        origin_key="doc-1",
        document_kind=DocumentKind.VIDEO,
        title="Discours de Marseille",
        original_url="https://example.org/video",
        author="Jean-Luc Mélenchon",
        published_at=datetime(2022, 4, 14),
    )

    sequence = DocumentarySequence(
        permanent_id="SEQ-0001",
        document_id="DOC-0001",
        start=timedelta(minutes=14, seconds=32),
        end=timedelta(minutes=15, seconds=18),
        text="Je suis favorable au retour de la retraite à 60 ans.",
    )

    piece = builder.build(document, sequence)

    assert piece.permanent_id == "SEQ-0001"
    assert piece.author == "Jean-Luc Mélenchon"
    assert piece.document_title == "Discours de Marseille"
    assert piece.sequence_text == (
        "Je suis favorable au retour de la retraite à 60 ans."
    )
    assert piece.document_url == document.original_url
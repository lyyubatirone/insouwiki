from datetime import datetime, timedelta

from insouwiki.domain.documentary_piece import DocumentaryPiece
from insouwiki.domain.verification_request import VerificationRequest
from insouwiki.services.simple_documentary_index import (
    SimpleDocumentaryIndex,
)


def test_find_returns_documentary_pieces():
    piece1 = DocumentaryPiece(
        permanent_id="PIECE-0001",
        author="Jean-Luc Mélenchon",
        document_title="Discours 1",
        published_at=datetime(2022, 4, 14),
        sequence_text="Première pièce documentaire.",
        sequence_start=timedelta(minutes=1),
        sequence_end=timedelta(minutes=2),
        document_url="https://example.org/video1",
    )

    piece2 = DocumentaryPiece(
        permanent_id="PIECE-0002",
        author="François Ruffin",
        document_title="Discours 2",
        published_at=datetime(2023, 5, 10),
        sequence_text="Deuxième pièce documentaire.",
        sequence_start=timedelta(minutes=5),
        sequence_end=timedelta(minutes=6),
        document_url="https://example.org/video2",
    )

    index = SimpleDocumentaryIndex(
        pieces=[piece1, piece2],
    )

    request = VerificationRequest(
        query="retraites",
    )

    result = index.find(request)

    assert len(result) == 2
    assert result[0] == piece1
    assert result[1] == piece2
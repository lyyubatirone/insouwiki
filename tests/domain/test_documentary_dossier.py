from datetime import datetime, timedelta

from insouwiki.domain.documentary_dossier import DocumentaryDossier
from insouwiki.domain.documentary_piece import DocumentaryPiece


def test_create_documentary_dossier():
    piece = DocumentaryPiece(
        permanent_id="PIECE-0001",
        author="Jean-Luc Mélenchon",
        document_title="Discours de Marseille",
        published_at=datetime(2022, 4, 14),
        sequence_text="La retraite doit être à 60 ans.",
        sequence_start=timedelta(minutes=14),
        sequence_end=timedelta(minutes=15),
        document_url="https://example.org/video",
    )

    dossier = DocumentaryDossier(
        title="Retraites",
        pieces=[piece],
    )

    assert dossier.title == "Retraites"
    assert len(dossier.pieces) == 1
    assert dossier.pieces[0].author == "Jean-Luc Mélenchon"
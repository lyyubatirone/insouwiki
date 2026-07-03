from datetime import datetime, timedelta

from insouwiki.domain.documentary_piece import DocumentaryPiece


def test_create_documentary_piece():
    piece = DocumentaryPiece(
        permanent_id="PIECE-00000001",
        author="Jean-Luc Mélenchon",
        document_title="Discours de Marseille",
        published_at=datetime(2022, 4, 14),
        sequence_text=(
            "Je suis favorable au retour de la retraite "
            "à 60 ans pour l'ensemble des salariés."
        ),
        sequence_start=timedelta(minutes=14, seconds=32),
        sequence_end=timedelta(minutes=15, seconds=18),
        document_url="https://example.org/document",
    )

    assert piece.author == "Jean-Luc Mélenchon"
    assert piece.document_title == "Discours de Marseille"
    assert (
        piece.sequence_text
        == "Je suis favorable au retour de la retraite à 60 ans pour l'ensemble des salariés."
    )
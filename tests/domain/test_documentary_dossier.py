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


def test_piece_count_returns_number_of_pieces():
    piece1 = DocumentaryPiece(
        permanent_id="PIECE-0001",
        author="Jean-Luc Mélenchon",
        document_title="Discours de Marseille",
        published_at=datetime(2022, 4, 14),
        sequence_text="Première déclaration.",
        sequence_start=timedelta(minutes=1),
        sequence_end=timedelta(minutes=2),
        document_url="https://example.org/video1",
    )

    piece2 = DocumentaryPiece(
        permanent_id="PIECE-0002",
        author="François Ruffin",
        document_title="Discours d'Amiens",
        published_at=datetime(2023, 5, 10),
        sequence_text="Deuxième déclaration.",
        sequence_start=timedelta(minutes=3),
        sequence_end=timedelta(minutes=4),
        document_url="https://example.org/video2",
    )

    dossier = DocumentaryDossier(
        title="Retraites",
        pieces=[piece1, piece2],
    )

    assert dossier.piece_count == 2


def test_document_count_counts_distinct_documents():
    piece1 = DocumentaryPiece(
        permanent_id="PIECE-0001",
        author="Jean-Luc Mélenchon",
        document_title="Discours de Marseille",
        published_at=datetime(2022, 4, 14),
        sequence_text="Première déclaration.",
        sequence_start=timedelta(minutes=1),
        sequence_end=timedelta(minutes=2),
        document_url="https://example.org/video1",
    )

    piece2 = DocumentaryPiece(
        permanent_id="PIECE-0002",
        author="Jean-Luc Mélenchon",
        document_title="Discours de Marseille",
        published_at=datetime(2022, 4, 14),
        sequence_text="Deuxième déclaration du même document.",
        sequence_start=timedelta(minutes=3),
        sequence_end=timedelta(minutes=4),
        document_url="https://example.org/video1",
    )

    piece3 = DocumentaryPiece(
        permanent_id="PIECE-0003",
        author="François Ruffin",
        document_title="Discours d'Amiens",
        published_at=datetime(2023, 5, 10),
        sequence_text="Déclaration issue d'un autre document.",
        sequence_start=timedelta(minutes=5),
        sequence_end=timedelta(minutes=6),
        document_url="https://example.org/video2",
    )

    dossier = DocumentaryDossier(
        title="Retraites",
        pieces=[piece1, piece2, piece3],
    )

    assert dossier.document_count == 2


def test_documented_personalities_returns_sorted_unique_names():
    piece1 = DocumentaryPiece(
        permanent_id="PIECE-0001",
        author="Jean-Luc Mélenchon",
        document_title="Discours de Marseille",
        published_at=datetime(2022, 4, 14),
        sequence_text="Première déclaration.",
        sequence_start=timedelta(minutes=1),
        sequence_end=timedelta(minutes=2),
        document_url="https://example.org/video1",
    )

    piece2 = DocumentaryPiece(
        permanent_id="PIECE-0002",
        author="François Ruffin",
        document_title="Discours d'Amiens",
        published_at=datetime(2023, 5, 10),
        sequence_text="Deuxième déclaration.",
        sequence_start=timedelta(minutes=3),
        sequence_end=timedelta(minutes=4),
        document_url="https://example.org/video2",
    )

    piece3 = DocumentaryPiece(
        permanent_id="PIECE-0003",
        author="Jean-Luc Mélenchon",
        document_title="Interview",
        published_at=datetime(2024, 2, 20),
        sequence_text="Troisième déclaration.",
        sequence_start=timedelta(minutes=5),
        sequence_end=timedelta(minutes=6),
        document_url="https://example.org/video3",
    )

    dossier = DocumentaryDossier(
        title="Retraites",
        pieces=[piece1, piece2, piece3],
    )

    assert dossier.documented_personalities == [
        "François Ruffin",
        "Jean-Luc Mélenchon",
    ]
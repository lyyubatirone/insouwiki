from datetime import datetime, timedelta

from insouwiki.domain.documentary_piece import DocumentaryPiece
from insouwiki.services.simple_documentary_dossier_builder import (
    SimpleDocumentaryDossierBuilder,
)


def test_build_documentary_dossier():
    builder = SimpleDocumentaryDossierBuilder()

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

    dossier = builder.build(
        title="Retraites",
        pieces=[piece],
    )

    assert dossier.title == "Retraites"
    assert len(dossier.pieces) == 1
    assert dossier.pieces[0].permanent_id == "PIECE-0001"


def test_build_orders_pieces_by_reverse_chronology():
    older_piece = DocumentaryPiece(
        permanent_id="PIECE-0001",
        author="Auteur",
        document_title="Document ancien",
        published_at=datetime(2022, 1, 1),
        sequence_text="Ancienne déclaration",
        sequence_start=timedelta(minutes=1),
        sequence_end=timedelta(minutes=2),
        document_url="https://example.org/old",
    )

    newer_piece = DocumentaryPiece(
        permanent_id="PIECE-0002",
        author="Auteur",
        document_title="Document récent",
        published_at=datetime(2024, 1, 1),
        sequence_text="Déclaration récente",
        sequence_start=timedelta(minutes=3),
        sequence_end=timedelta(minutes=4),
        document_url="https://example.org/new",
    )

    builder = SimpleDocumentaryDossierBuilder()

    dossier = builder.build(
        title="Chronologie",
        pieces=[older_piece, newer_piece],
    )

    assert dossier.pieces == [
        newer_piece,
        older_piece,
    ]
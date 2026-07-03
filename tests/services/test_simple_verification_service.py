from datetime import datetime, timedelta

from insouwiki.domain.documentary_piece import DocumentaryPiece
from insouwiki.domain.verification_request import VerificationRequest
from insouwiki.services.simple_documentary_dossier_builder import (
    SimpleDocumentaryDossierBuilder,
)
from insouwiki.services.simple_documentary_index import (
    SimpleDocumentaryIndex,
)
from insouwiki.services.simple_verification_service import (
    SimpleVerificationService,
)


def test_verify_builds_documentary_dossier():
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

    index = SimpleDocumentaryIndex(
        pieces=[piece],
    )

    dossier_builder = SimpleDocumentaryDossierBuilder()

    service = SimpleVerificationService(
        documentary_index=index,
        dossier_builder=dossier_builder,
    )

    request = VerificationRequest(
        query="Retraites",
    )

    dossier = service.verify(request)

    assert dossier.title == "Retraites"
    assert len(dossier.pieces) == 1
    assert dossier.pieces[0] == piece
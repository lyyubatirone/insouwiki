from insouwiki.domain.documentary_dossier import DocumentaryDossier
from insouwiki.domain.verification_request import VerificationRequest
from insouwiki.services.documentary_dossier_builder import (
    DocumentaryDossierBuilder,
)
from insouwiki.services.documentary_index import DocumentaryIndex
from insouwiki.services.verification_service import VerificationService


class SimpleVerificationService(VerificationService):
    """
    Première implémentation du moteur de vérification documentaire.

    Cette version orchestre l'index documentaire et
    le constructeur de dossiers documentaires.
    """

    def __init__(
        self,
        documentary_index: DocumentaryIndex,
        dossier_builder: DocumentaryDossierBuilder,
    ):
        self._documentary_index = documentary_index
        self._dossier_builder = dossier_builder

    def verify(
        self,
        request: VerificationRequest,
    ) -> DocumentaryDossier:
        pieces = self._documentary_index.find(request)

        return self._dossier_builder.build(
            title=request.query,
            pieces=pieces,
        )
from abc import ABC, abstractmethod

from insouwiki.domain.documentary_dossier import DocumentaryDossier
from insouwiki.domain.verification_request import VerificationRequest


class VerificationService(ABC):
    """
    Service de vérification documentaire.

    Transforme une demande de vérification documentaire
    en dossier documentaire.
    """

    @abstractmethod
    def verify(
        self,
        request: VerificationRequest,
    ) -> DocumentaryDossier:
        raise NotImplementedError
from abc import ABC, abstractmethod

from insouwiki.domain.documentary_piece import DocumentaryPiece
from insouwiki.domain.verification_request import VerificationRequest


class DocumentaryIndex(ABC):
    """
    Index documentaire.

    Retrouve les pièces documentaires correspondant
    à une demande de vérification documentaire.
    """

    @abstractmethod
    def find(
        self,
        request: VerificationRequest,
    ) -> list[DocumentaryPiece]:
        raise NotImplementedError
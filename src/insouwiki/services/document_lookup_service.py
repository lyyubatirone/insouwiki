from abc import ABC, abstractmethod

from insouwiki.domain.document import Document


class DocumentLookupService(ABC):
    """
    Recherche des documents documentaires.
    """

    @abstractmethod
    def get_by_url(
        self,
        url: str,
    ) -> Document | None:
        """
        Retourne le document correspondant à une URL.
        """
        ...
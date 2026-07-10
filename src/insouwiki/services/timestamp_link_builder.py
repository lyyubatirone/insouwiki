from abc import ABC, abstractmethod

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_sequence import DocumentarySequence


class TimestampLinkBuilder(ABC):
    """
    Construit un lien vers la source au moment
    où commence une séquence documentaire.
    """

    @abstractmethod
    def build(
        self,
        document: Document,
        sequence: DocumentarySequence,
    ) -> str:
        """
        Produit un lien horodaté vers la source documentaire.
        """
        ...
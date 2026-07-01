from abc import ABC, abstractmethod

from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_sequence import DocumentarySequence


class DocumentaryFactExtractor(ABC):
    """
    Transforme des séquences documentaires
    en faits documentaires.
    """

    @abstractmethod
    def extract(
        self,
        sequences: list[DocumentarySequence],
    ) -> list[DocumentaryFact]:
        """
        Produit les faits documentaires observables
        à partir des séquences.
        """
        ...
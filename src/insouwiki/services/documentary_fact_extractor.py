from abc import ABC, abstractmethod

from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_sequence import DocumentarySequence


class DocumentaryFactExtractor(ABC):
    """
    Extrait des faits documentaires
    à partir de séquences documentaires.
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
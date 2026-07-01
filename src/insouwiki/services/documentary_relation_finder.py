from abc import ABC, abstractmethod

from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_relation import DocumentaryRelation


class DocumentaryRelationFinder(ABC):
    """
    Trouve des relations documentaires entre faits documentaires.
    """

    @abstractmethod
    def find(
        self,
        facts: list[DocumentaryFact],
    ) -> list[DocumentaryRelation]:
        """
        Produit les relations documentaires observables
        entre les faits fournis.
        """
        ...
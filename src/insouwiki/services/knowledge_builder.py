from abc import ABC, abstractmethod

from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_relation import DocumentaryRelation
from insouwiki.domain.knowledge import Knowledge


class KnowledgeBuilder(ABC):
    """
    Construit des connaissances documentaires
    à partir de faits et de relations documentaires.
    """

    @abstractmethod
    def build(
        self,
        facts: list[DocumentaryFact],
        relations: list[DocumentaryRelation],
    ) -> list[Knowledge]:
        """
        Produit des connaissances documentaires explicables.
        """
        ...
from abc import ABC, abstractmethod

from insouwiki.domain.documentary_exploration import DocumentaryExploration
from insouwiki.domain.documentary_inventory import DocumentaryInventory


class DocumentaryRepository(ABC):
    """
    Représente un patrimoine documentaire interrogeable.
    """

    @abstractmethod
    def explore(
        self,
        exploration: DocumentaryExploration,
    ) -> DocumentaryInventory:
        """
        Établit un inventaire documentaire correspondant
        à l'exploration demandée.
        """
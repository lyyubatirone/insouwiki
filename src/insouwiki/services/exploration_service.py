from abc import ABC, abstractmethod

from insouwiki.domain.documentary_exploration import DocumentaryExploration
from insouwiki.domain.exploration_intent import ExplorationIntent


class ExplorationService(ABC):
    """
    Point d'entrée des explorations documentaires.

    Ce service orchestre la construction d'une exploration
    à partir d'une intention et d'une porte d'entrée.
    """

    @abstractmethod
    def explore(
        self,
        intent: ExplorationIntent,
        entry_point: str,
    ) -> DocumentaryExploration:
        raise NotImplementedError
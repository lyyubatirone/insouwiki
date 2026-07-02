from abc import ABC, abstractmethod

from insouwiki.domain.documentary_exploration import DocumentaryExploration
from insouwiki.domain.exploration_intent import ExplorationIntent


class ExplorationBuilder(ABC):
    """
    Construit une exploration documentaire à partir
    d'une intention, d'une porte d'entrée et
    d'observations documentaires.
    """

    @abstractmethod
    def build(
        self,
        intent: ExplorationIntent,
        entry_point: str,
        observations: list[str],
    ) -> DocumentaryExploration:
        raise NotImplementedError
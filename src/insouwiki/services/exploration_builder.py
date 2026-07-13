from abc import ABC, abstractmethod

from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)


class ExplorationBuilder(ABC):
    """
    Construit une exploration documentaire à partir
    d'une intention, d'une question documentaire
    et d'observations documentaires.
    """

    @abstractmethod
    def build(
        self,
        intent: ExplorationIntent,
        question: DocumentaryQuestion,
        observations: list[str],
    ) -> DocumentaryExploration:
        ...
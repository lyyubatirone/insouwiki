from insouwiki.domain.documentary_exploration import DocumentaryExploration
from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.exploration_intent import ExplorationIntent
from insouwiki.services.continuity_finder import ContinuityFinder
from insouwiki.services.exploration_builder import ExplorationBuilder
from insouwiki.services.exploration_service import ExplorationService


class SimpleExplorationService(ExplorationService):
    """
    Première implémentation du service d'exploration.

    Cette version orchestre la construction d'une exploration
    documentaire en utilisant un raisonneur de continuité.
    """

    def __init__(
        self,
        builder: ExplorationBuilder,
        continuity_finder: ContinuityFinder,
    ) -> None:
        self._builder = builder
        self._continuity_finder = continuity_finder

    def explore(
        self,
        intent: ExplorationIntent,
        entry_point: str,
        facts: list[DocumentaryFact],
    ) -> DocumentaryExploration:
        observations = self._continuity_finder.find(facts)

        return self._builder.build(
            intent=intent,
            entry_point=entry_point,
            observations=observations,
        )
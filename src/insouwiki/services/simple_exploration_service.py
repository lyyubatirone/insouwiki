from insouwiki.domain.documentary_exploration import DocumentaryExploration
from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.exploration_intent import ExplorationIntent
from insouwiki.services.continuity_finder import ContinuityFinder
from insouwiki.services.convergence_finder import ConvergenceFinder
from insouwiki.services.divergence_finder import DivergenceFinder
from insouwiki.services.evolution_finder import EvolutionFinder
from insouwiki.services.exploration_builder import ExplorationBuilder
from insouwiki.services.exploration_service import ExplorationService


class SimpleExplorationService(ExplorationService):
    """
    Première implémentation du service d'exploration.

    Cette version orchestre la construction d'une exploration
    documentaire en utilisant les premiers raisonneurs documentaires.
    """

    def __init__(
        self,
        builder: ExplorationBuilder,
        continuity_finder: ContinuityFinder,
        evolution_finder: EvolutionFinder,
        convergence_finder: ConvergenceFinder,
        divergence_finder: DivergenceFinder,
    ) -> None:
        self._builder = builder
        self._continuity_finder = continuity_finder
        self._evolution_finder = evolution_finder
        self._convergence_finder = convergence_finder
        self._divergence_finder = divergence_finder

    def explore(
        self,
        intent: ExplorationIntent,
        entry_point: str,
        facts: list[DocumentaryFact],
    ) -> DocumentaryExploration:
        observations = []

        observations.extend(
            self._continuity_finder.find(facts)
        )

        evolutions = self._evolution_finder.find(facts)

        observations.extend(
            evolution.summary
            for evolution in evolutions
        )

        observations.extend(
            self._convergence_finder.find(facts)
        )

        observations.extend(
            self._divergence_finder.find(facts)
        )

        return self._builder.build(
            intent=intent,
            entry_point=entry_point,
            observations=observations,
        )
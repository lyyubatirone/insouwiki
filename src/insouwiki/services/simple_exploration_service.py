from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)
from insouwiki.services.continuity_finder import ContinuityFinder
from insouwiki.services.convergence_finder import ConvergenceFinder
from insouwiki.services.divergence_finder import DivergenceFinder
from insouwiki.services.evolution_finder import EvolutionFinder
from insouwiki.services.exploration_builder import (
    ExplorationBuilder,
)
from insouwiki.services.exploration_service import (
    ExplorationService,
)
from insouwiki.services.documentary_question_interpreter import (
    DocumentaryQuestionInterpreter,
)

class SimpleExplorationService(ExplorationService):
    """
    Orchestre la construction d'une exploration documentaire.

    Ce service coordonne plusieurs finders documentaires,
    puis délègue la construction finale à un builder.
    """

    def __init__(
        self,
        builder: ExplorationBuilder,
        question_interpreter: DocumentaryQuestionInterpreter,
        continuity_finder: ContinuityFinder,
        evolution_finder: EvolutionFinder,
        convergence_finder: ConvergenceFinder,
        divergence_finder: DivergenceFinder,
    ) -> None:
        self._builder = builder
        self._question_interpreter = question_interpreter
        self._continuity_finder = continuity_finder
        self._evolution_finder = evolution_finder
        self._convergence_finder = convergence_finder
        self._divergence_finder = divergence_finder

    def explore(
        self,
        intent: ExplorationIntent,
        question: DocumentaryQuestion,
        facts: list[DocumentaryFact],
    ) -> DocumentaryExploration:
        observations: list[str] = []

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

        subjects, criteria = (
            self._question_interpreter.interpret(
                question,
            )
        )

        return self._builder.build(
            intent=intent,
            question=question,
            subjects=subjects,
            criteria=criteria,
            observations=observations,
        )
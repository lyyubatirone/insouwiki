from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)
from insouwiki.services.exploration_builder import (
    ExplorationBuilder,
)
from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from insouwiki.domain.documentary_subject import (
    DocumentarySubject,
)


class SimpleExplorationBuilder(ExplorationBuilder):
    """
    Première implémentation de l'Exploration Builder.

    Cette version construit une exploration documentaire minimale
    à partir d'une intention, d'une question documentaire
    et d'observations déjà produites.
    """

    def build(
        self,
        intent: ExplorationIntent,
        question: DocumentaryQuestion,
        subjects: list[DocumentarySubject],
        criteria: tuple[DocumentaryCriterion, ...],
        observations: list[str],
    ) -> DocumentaryExploration:
        return DocumentaryExploration(
            intent=intent,
            question=question,
            criteria=criteria,
            subjects=[
                subject.label
                for subject in subjects
            ],
            observations=observations,
        )
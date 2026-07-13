from dataclasses import dataclass

from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)
from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class DocumentaryExploration:
    intent: ExplorationIntent
    question: DocumentaryQuestion
    criteria: tuple[DocumentaryCriterion, ...]
    subjects: list[str]
    observations: list[str]

    def refine(
        self,
        criterion: DocumentaryCriterion,
    ) -> "DocumentaryExploration":
        return replace(
            self,
            criteria=(
                *self.criteria,
                criterion,
            ),
        )


from dataclasses import dataclass, replace

from insouwiki.domain.documentary_criterion import DocumentaryCriterion
from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)


@dataclass(frozen=True)
class DocumentaryRequest:
    text: str
    criteria: tuple[DocumentaryCriterion, ...] = ()

    def refine(
        self,
        criterion: DocumentaryCriterion,
    ) -> "DocumentaryRequest":
        return replace(
            self,
            criteria=(
                *self.criteria,
                criterion,
            ),
        )
    def remove(
        self,
        criterion: DocumentaryCriterion,
    ) -> "DocumentaryRequest":
        return replace(
            self,
            criteria=tuple(
                existing_criterion
                for existing_criterion in self.criteria
                if existing_criterion != criterion
            ),
        )
    def start(self) -> DocumentaryExploration:
        return DocumentaryExploration(
            intent=ExplorationIntent.UNDERSTAND,
            question=DocumentaryQuestion(
                text=self.text,
            ),
            criteria=self.criteria,
            subjects=[],
            observations=[],
        )
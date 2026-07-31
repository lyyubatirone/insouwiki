from dataclasses import dataclass, replace
from typing import Protocol, TypeVar

from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)


InventoryT = TypeVar("InventoryT")


class DocumentaryRepositoryProtocol(Protocol):
    def explore(
        self,
        exploration: "DocumentaryExploration",
    ) -> InventoryT:
        ...


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

    def remove(
        self,
        criterion: DocumentaryCriterion,
    ) -> "DocumentaryExploration":
        return replace(
            self,
            criteria=tuple(
                existing_criterion
                for existing_criterion in self.criteria
                if existing_criterion != criterion
            ),
        )

    def explore(
        self,
        repository: DocumentaryRepositoryProtocol,
    ) -> InventoryT:
        return repository.explore(self)
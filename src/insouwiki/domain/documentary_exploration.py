from dataclasses import dataclass

from insouwiki.domain.exploration_intent import ExplorationIntent


@dataclass(frozen=True)
class DocumentaryExploration:
    """
    Première représentation d'une exploration documentaire.

    Une exploration documentaire incarne une intention
    du lecteur et rassemble les premiers éléments permettant
    d'organiser son parcours documentaire.
    """

    intent: ExplorationIntent

    subjects: list[str]

    observations: list[str]
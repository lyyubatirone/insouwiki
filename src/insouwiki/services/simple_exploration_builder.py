from insouwiki.domain.documentary_exploration import DocumentaryExploration
from insouwiki.domain.exploration_intent import ExplorationIntent
from insouwiki.services.exploration_builder import ExplorationBuilder


class SimpleExplorationBuilder(ExplorationBuilder):
    """
    Première implémentation de l'Exploration Builder.

    Cette version construit une exploration documentaire minimale
    à partir d'une intention, d'une porte d'entrée et d'observations
    documentaires déjà produites.
    """

    def build(
        self,
        intent: ExplorationIntent,
        entry_point: str,
        observations: list[str],
    ) -> DocumentaryExploration:
        return DocumentaryExploration(
            intent=intent,
            subjects=[
                entry_point,
            ],
            observations=observations,
        )
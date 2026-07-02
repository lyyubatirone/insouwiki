from insouwiki.domain.documentary_evolution import DocumentaryEvolution
from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.evolution_finder import EvolutionFinder


class SimpleEvolutionFinder(EvolutionFinder):
    """
    Première implémentation de la recherche
    d'évolutions documentaires.

    Cette version applique uniquement les règles
    minimales de prudence documentaire.
    """

    def find(
        self,
        facts: list[DocumentaryFact],
    ) -> list[DocumentaryEvolution]:
        if len(facts) < 2:
            return []

        return []
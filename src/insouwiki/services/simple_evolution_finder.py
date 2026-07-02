from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.evolution_finder import EvolutionFinder


class SimpleEvolutionFinder(EvolutionFinder):
    """
    Première implémentation de la recherche
    d'évolutions documentaires.

    Cette version ne détecte encore aucune évolution.
    Elle établit uniquement les conditions minimales
    nécessaires avant de commencer une analyse.
    """

    def find(
        self,
        facts: list[DocumentaryFact],
    ):
        if len(facts) < 2:
            return []

        return []
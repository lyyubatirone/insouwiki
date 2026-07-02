from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.divergence_finder import DivergenceFinder


class SimpleDivergenceFinder(DivergenceFinder):
    """
    Première implémentation de la recherche
    de divergences documentaires.
    """

    def find(
        self,
        facts: list[DocumentaryFact],
    ) -> list[str]:
        if len(facts) < 2:
            return []

        first_statement = facts[0].statement
        authors = {
            fact.author
            for fact in facts
        }

        if len(authors) < 2:
            return []

        for fact in facts:
            if fact.statement == first_statement:
                continue

            return [
                "Plusieurs auteurs expriment des affirmations différentes sur ce sujet dans les sources documentaires disponibles."
            ]

        return []
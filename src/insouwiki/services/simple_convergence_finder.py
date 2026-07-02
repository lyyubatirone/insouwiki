from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.convergence_finder import ConvergenceFinder


class SimpleConvergenceFinder(ConvergenceFinder):
    """
    Première implémentation de la recherche
    de convergences documentaires.
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
            if fact.statement != first_statement:
                return []

        return [
            "Plusieurs auteurs expriment une affirmation similaire sur ce sujet dans les sources documentaires disponibles."
        ]
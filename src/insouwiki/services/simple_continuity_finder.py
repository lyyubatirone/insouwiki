from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.continuity_finder import ContinuityFinder


class SimpleContinuityFinder(ContinuityFinder):
    """
    Première implémentation de la recherche
    de continuités documentaires.
    """

    def find(
        self,
        facts: list[DocumentaryFact],
    ) -> list[str]:
        if len(facts) < 3:
            return []

        first_statement = facts[0].statement

        for fact in facts:
            if fact.statement != first_statement:
                return []

        return [
            "Cette affirmation apparaît de manière récurrente dans les sources documentaires disponibles."
        ]
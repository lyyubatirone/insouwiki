from insouwiki.domain.documentary_evolution import DocumentaryEvolution
from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.services.evolution_finder import EvolutionFinder


class SimpleEvolutionFinder(EvolutionFinder):
    """
    Première implémentation de la recherche
    d'évolutions documentaires.
    """

    def find(
        self,
        facts: list[DocumentaryFact],
    ) -> list[DocumentaryEvolution]:
        if len(facts) < 2:
            return []

        first_fact = facts[0]
        second_fact = facts[1]

        first_statement = first_fact.statement.strip().rstrip(".")
        second_statement = second_fact.statement.strip().rstrip(".")

        if first_statement == second_statement:
            return []

        if (
            second_statement.startswith(first_statement)
            or first_statement.startswith(second_statement)
        ):
            return []

        return [
            DocumentaryEvolution(
                permanent_id="EVOL-00000001",
                supporting_fact_ids=[
                    first_fact.permanent_id,
                    second_fact.permanent_id,
                ],
                summary="Une évolution documentaire est observable entre ces faits.",
            )
        ]
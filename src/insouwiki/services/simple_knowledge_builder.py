from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_relation import DocumentaryRelation
from insouwiki.domain.knowledge import Knowledge
from insouwiki.services.knowledge_builder import KnowledgeBuilder


class SimpleKnowledgeBuilder(KnowledgeBuilder):
    """
    Première implémentation du constructeur de connaissances.

    Version 1 :
    regroupe tous les faits fournis dans une seule connaissance.
    """

    def build(
        self,
        facts: list[DocumentaryFact],
        relations: list[DocumentaryRelation],
    ) -> list[Knowledge]:
        if len(facts) == 0:
            return []

        return [
            Knowledge(
                permanent_id="KNOW-00000001",
                title="Connaissance documentaire",
                summary=(
                    "Cette connaissance documentaire est construite "
                    f"à partir de {len(facts)} fait(s) documentaire(s) "
                    f"et {len(relations)} relation(s) documentaire(s)."
                ),
                supporting_fact_ids=[
                    fact.permanent_id for fact in facts
                ],
            )
        ]
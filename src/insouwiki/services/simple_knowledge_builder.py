from collections import defaultdict

from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_relation import DocumentaryRelation
from insouwiki.domain.knowledge import Knowledge
from insouwiki.services.knowledge_builder import KnowledgeBuilder


class SimpleKnowledgeBuilder(KnowledgeBuilder):
    """
    Première implémentation du constructeur de connaissances.

    Version 2 :
    regroupe les faits par auteur.
    """

    def build(
        self,
        facts: list[DocumentaryFact],
        relations: list[DocumentaryRelation],
    ) -> list[Knowledge]:
        if len(facts) == 0:
            return []

        facts_by_author: dict[str, list[DocumentaryFact]] = defaultdict(list)

        for fact in facts:
            facts_by_author[fact.author].append(fact)

        knowledge_items: list[Knowledge] = []

        for index, (author, author_facts) in enumerate(
            facts_by_author.items(),
            start=1,
        ):
            knowledge_items.append(
                Knowledge(
                    permanent_id=f"KNOW-{index:08d}",
                    title=f"Connaissance documentaire — {author}",
                    summary=(
                        "Cette connaissance documentaire regroupe "
                        f"{len(author_facts)} fait(s) documentaire(s) "
                        f"attribué(s) à {author}."
                    ),
                    supporting_fact_ids=[
                        fact.permanent_id for fact in author_facts
                    ],
                )
            )

        return knowledge_items
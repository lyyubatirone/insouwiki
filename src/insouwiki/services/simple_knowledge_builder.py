from collections import defaultdict, deque

from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_relation import DocumentaryRelation
from insouwiki.domain.knowledge import Knowledge
from insouwiki.services.knowledge_builder import KnowledgeBuilder


class SimpleKnowledgeBuilder(KnowledgeBuilder):
    """
    Première implémentation du constructeur de connaissances.

    Version 3 :
    regroupe les faits connectés par des relations documentaires.
    """

    def build(
        self,
        facts: list[DocumentaryFact],
        relations: list[DocumentaryRelation],
    ) -> list[Knowledge]:
        if len(facts) == 0:
            return []

        facts_by_id = {
            fact.permanent_id: fact
            for fact in facts
        }

        graph: dict[str, set[str]] = defaultdict(set)

        for fact in facts:
            graph[fact.permanent_id]

        for relation in relations:
            if (
                relation.source_fact_id in facts_by_id
                and relation.target_fact_id in facts_by_id
            ):
                graph[relation.source_fact_id].add(relation.target_fact_id)
                graph[relation.target_fact_id].add(relation.source_fact_id)

        visited: set[str] = set()
        groups: list[list[DocumentaryFact]] = []

        for fact in facts:
            if fact.permanent_id in visited:
                continue

            group: list[DocumentaryFact] = []
            queue: deque[str] = deque([fact.permanent_id])
            visited.add(fact.permanent_id)

            while queue:
                current_id = queue.popleft()
                current_fact = facts_by_id[current_id]
                group.append(current_fact)

                for neighbor_id in graph[current_id]:
                    if neighbor_id not in visited:
                        visited.add(neighbor_id)
                        queue.append(neighbor_id)

            groups.append(group)

        knowledge_items: list[Knowledge] = []

        for index, group in enumerate(groups, start=1):
            knowledge_items.append(
                Knowledge(
                    permanent_id=f"KNOW-{index:08d}",
                    title=f"Connaissance documentaire {index}",
                    summary=(
                        "Cette connaissance documentaire regroupe "
                        f"{len(group)} fait(s) documentaire(s) relié(s)."
                    ),
                    supporting_fact_ids=[
                        fact.permanent_id for fact in group
                    ],
                )
            )

        return knowledge_items
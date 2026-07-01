from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_relation import DocumentaryRelation
from insouwiki.domain.documentary_relation_type import DocumentaryRelationType
from insouwiki.services.documentary_relation_finder import (
    DocumentaryRelationFinder,
)


class SimpleDocumentaryRelationFinder(DocumentaryRelationFinder):
    """
    Première implémentation du chercheur de relations documentaires.

    Version 1 :
    si plusieurs faits ont le même auteur, une relation SAME_AUTHOR
    est créée entre eux.
    """

    def find(
        self,
        facts: list[DocumentaryFact],
    ) -> list[DocumentaryRelation]:
        relations: list[DocumentaryRelation] = []

        relation_index = 1

        for source_index, source_fact in enumerate(facts):
            for target_fact in facts[source_index + 1 :]:
                if source_fact.author == target_fact.author:
                    relations.append(
                        DocumentaryRelation(
                            permanent_id=f"REL-{relation_index:08d}",
                            relation_type=DocumentaryRelationType.SAME_AUTHOR,
                            source_fact_id=source_fact.permanent_id,
                            target_fact_id=target_fact.permanent_id,
                        )
                    )
                    relation_index += 1

        return relations
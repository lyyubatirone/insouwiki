from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_relation import DocumentaryRelation
from insouwiki.domain.documentary_relation_type import DocumentaryRelationType
from insouwiki.services.documentary_relation_finder import (
    DocumentaryRelationFinder,
)


class SimpleDocumentaryRelationFinder(DocumentaryRelationFinder):
    """
    Recherche des relations documentaires entre faits documentaires.

    Cette première règle relie les faits attribués au même auteur.
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
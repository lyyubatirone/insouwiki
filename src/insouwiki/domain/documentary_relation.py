from pydantic import BaseModel

from insouwiki.domain.documentary_relation_type import DocumentaryRelationType


class DocumentaryRelation(BaseModel):
    """
    Relation documentaire entre deux faits documentaires.

    Une relation qualifie le lien observable entre deux faits.
    Elle ne modifie jamais les faits qu'elle relie.
    """

    permanent_id: str

    relation_type: DocumentaryRelationType

    source_fact_id: str

    target_fact_id: str
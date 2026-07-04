from pydantic import BaseModel

from insouwiki.domain.documentary_entity import DocumentaryEntity
from insouwiki.domain.documentary_entity_relation_type import (
    DocumentaryEntityRelationType,
)


class DocumentaryEntityRelation(BaseModel):
    """
    Relation documentaire entre deux entités.

    Une relation documentaire relie une entité source
    à une entité cible selon un type de relation explicite.
    """

    source: DocumentaryEntity

    relation_type: DocumentaryEntityRelationType

    target: DocumentaryEntity
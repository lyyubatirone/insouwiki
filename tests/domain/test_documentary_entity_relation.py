from insouwiki.domain.documentary_entity import DocumentaryEntity
from insouwiki.domain.documentary_entity_relation import (
    DocumentaryEntityRelation,
)
from insouwiki.domain.documentary_entity_relation_type import (
    DocumentaryEntityRelationType,
)
from insouwiki.domain.documentary_entity_type import DocumentaryEntityType


def test_documentary_entity_relation_links_two_entities():
    person = DocumentaryEntity(
        permanent_id="ENTITY-000001",
        entity_type=DocumentaryEntityType.PERSON,
        name="Mathilde Panot",
    )

    parliamentary_group = DocumentaryEntity(
        permanent_id="ENTITY-000002",
        entity_type=DocumentaryEntityType.PARLIAMENTARY_GROUP,
        name="Groupe LFI–NFP",
    )

    relation = DocumentaryEntityRelation(
        source=person,
        relation_type=DocumentaryEntityRelationType.MEMBER_OF,
        target=parliamentary_group,
    )

    assert relation.source == person
    assert relation.target == parliamentary_group
    assert (
        relation.relation_type
        == DocumentaryEntityRelationType.MEMBER_OF
    )
from insouwiki.domain.documentary_entity import DocumentaryEntity


def test_documentary_entity_has_identity():
    entity = DocumentaryEntity(
        permanent_id="ENTITY-000001",
        entity_type="PERSON",
        name="Jean-Luc Mélenchon",
    )

    assert entity.permanent_id == "ENTITY-000001"
    assert entity.entity_type == "PERSON"
    assert entity.name == "Jean-Luc Mélenchon"
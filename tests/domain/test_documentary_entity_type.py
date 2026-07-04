from insouwiki.domain.documentary_entity_type import DocumentaryEntityType


def test_documentary_entity_type_values():
    assert DocumentaryEntityType.PERSON == "PERSON"
    assert DocumentaryEntityType.INSTITUTION == "INSTITUTION"
    assert (
        DocumentaryEntityType.POLITICAL_ORGANIZATION
        == "POLITICAL_ORGANIZATION"
    )
    assert (
        DocumentaryEntityType.PARLIAMENTARY_GROUP
        == "PARLIAMENTARY_GROUP"
    )
    assert (
        DocumentaryEntityType.PARLIAMENTARY_COMMISSION
        == "PARLIAMENTARY_COMMISSION"
    )
    assert DocumentaryEntityType.PLACE == "PLACE"
    assert DocumentaryEntityType.EVENT == "EVENT"
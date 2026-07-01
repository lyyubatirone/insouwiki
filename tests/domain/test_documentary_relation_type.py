from insouwiki.domain.documentary_relation_type import (
    DocumentaryRelationType,
)


def test_documentary_relation_type_values():
    assert DocumentaryRelationType.SAME_AUTHOR.value == "same_author"
    assert DocumentaryRelationType.SAME_TOPIC.value == "same_topic"
    assert DocumentaryRelationType.SAME_EVENT.value == "same_event"

    assert DocumentaryRelationType.CHRONOLOGY.value == "chronology"

    assert DocumentaryRelationType.COMPLEMENTS.value == "complements"
    assert DocumentaryRelationType.REFINES.value == "refines"

    assert DocumentaryRelationType.CONSISTENT.value == "consistent"
    assert DocumentaryRelationType.CONTRADICTS.value == "contradicts"

    assert DocumentaryRelationType.EVOLUTION.value == "evolution"


def test_documentary_relation_type_is_complete():
    assert len(DocumentaryRelationType) == 9
from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)


def test_documentary_criterion_keeps_field_and_value():
    criterion = DocumentaryCriterion(
        field="author",
        value="Jean-Luc Mélenchon",
    )

    assert criterion.field == "author"
    assert (
        criterion.value
        == "Jean-Luc Mélenchon"
    )
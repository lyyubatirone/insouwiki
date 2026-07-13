from datetime import date

from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from insouwiki.domain.documentary_date_range import (
    DocumentaryDateRange,
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

def test_criterion_accepts_documentary_date_range():
    date_range = DocumentaryDateRange(
        start=date(2020, 1, 1),
        end=date(2022, 12, 31),
    )

    criterion = DocumentaryCriterion(
        field="date de publication",
        value=date_range,
    )

    assert criterion.value == date_range
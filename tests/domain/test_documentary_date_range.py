from datetime import date

from insouwiki.domain.documentary_date_range import (
    DocumentaryDateRange,
)


def test_create_documentary_date_range():
    date_range = DocumentaryDateRange(
        start=date(2020, 1, 1),
        end=date(2022, 12, 31),
    )

    assert date_range.start == date(2020, 1, 1)
    assert date_range.end == date(2022, 12, 31)
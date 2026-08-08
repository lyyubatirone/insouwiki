from datetime import date

from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)


def test_date_inside_documentary_period():
    period = DocumentaryPeriod(
        label="Campagne présidentielle 2022",
        starts_at=date(2022, 3, 7),
        ends_at=date(2022, 4, 24),
    )

    assert period.contains(
        date(2022, 4, 12),
    )


def test_date_before_documentary_period():
    period = DocumentaryPeriod(
        label="Campagne présidentielle 2022",
        starts_at=date(2022, 3, 7),
        ends_at=date(2022, 4, 24),
    )

    assert not period.contains(
        date(2022, 2, 1),
    )


def test_date_after_documentary_period():
    period = DocumentaryPeriod(
        label="Campagne présidentielle 2022",
        starts_at=date(2022, 3, 7),
        ends_at=date(2022, 4, 24),
    )

    assert not period.contains(
        date(2022, 5, 1),
    )
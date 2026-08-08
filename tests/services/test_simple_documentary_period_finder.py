from datetime import date

from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)
from insouwiki.services.simple_documentary_period_finder import (
    SimpleDocumentaryPeriodFinder,
)


class InMemoryDocumentaryPeriodRepository:
    def __init__(
        self,
        periods: tuple[DocumentaryPeriod, ...],
    ):
        self.periods = periods

    def list_all(
        self,
    ) -> tuple[DocumentaryPeriod, ...]:
        return self.periods


def test_finds_all_documentary_periods_for_date():
    periods = (
        DocumentaryPeriod(
            label="Mandat présidentiel 2017–2022",
            starts_at=date(2017, 5, 14),
            ends_at=date(2022, 5, 13),
        ),
        DocumentaryPeriod(
            label="Campagne présidentielle 2022",
            starts_at=date(2022, 3, 7),
            ends_at=date(2022, 4, 24),
        ),
        DocumentaryPeriod(
            label="XVe législature (2017–2022)",
            starts_at=date(2017, 6, 21),
            ends_at=date(2022, 6, 21),
        ),
    )

    repository = InMemoryDocumentaryPeriodRepository(
        periods,
    )

    finder = SimpleDocumentaryPeriodFinder(
        repository=repository,
    )

    finder = SimpleDocumentaryPeriodFinder(
        repository=repository,
    )

    result = finder.find_all_for(
        date(2022, 4, 12),
    )

    assert result == periods
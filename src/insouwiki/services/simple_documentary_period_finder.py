from datetime import date

from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)
from insouwiki.domain.documentary_period_repository import (
    DocumentaryPeriodRepository,
)


class SimpleDocumentaryPeriodFinder:
    """Trouve les périodes documentaires correspondant à une date."""

    def __init__(
        self,
        repository: DocumentaryPeriodRepository,
    ):
        self.repository = repository

    def find_all_for(
        self,
        current_date: date,
    ) -> tuple[DocumentaryPeriod, ...]:
        return tuple(
            period
            for period in self.repository.list_all()
            if period.contains(current_date)
        )
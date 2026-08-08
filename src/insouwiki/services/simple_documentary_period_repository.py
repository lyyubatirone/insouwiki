from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)
from insouwiki.domain.documentary_period_repository import (
    DocumentaryPeriodRepository,
)


class SimpleDocumentaryPeriodRepository(
    DocumentaryPeriodRepository,
):
    """
    Référentiel simple des périodes documentaires.
    """

    def __init__(
        self,
        periods: tuple[DocumentaryPeriod, ...],
    ):
        self.periods = periods

    def list_all(
        self,
    ) -> tuple[DocumentaryPeriod, ...]:
        return self.periods

    def register(
        self,
        period: DocumentaryPeriod,
    ) -> DocumentaryPeriod:
        self.periods = (
            *self.periods,
            period,
        )

        return period

    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> DocumentaryPeriod | None:
        for period in self.periods:
            if period.permanent_id == permanent_id:
                return period

        return None
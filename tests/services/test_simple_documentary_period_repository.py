from datetime import date

from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)
from insouwiki.services.simple_documentary_period_repository import (
    SimpleDocumentaryPeriodRepository,
)


def test_lists_documentary_periods():
    periods = (
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

    repository = SimpleDocumentaryPeriodRepository(
        periods=periods,
    )

    assert repository.list_all() == periods

def test_registers_documentary_period():
    repository = SimpleDocumentaryPeriodRepository(
        periods=(),
    )

    period = DocumentaryPeriod(
        permanent_id="PRD-00000001",
        label="Campagne présidentielle 2027",
        starts_at=date(2026, 1, 1),
        definition=(
            "La période débute avec la première "
            "déclaration officielle de candidature."
        ),
    )

    result = repository.register(period)

    assert result == period
    assert repository.list_all() == (
        period,
    )

def test_gets_documentary_period_by_permanent_id():
    period = DocumentaryPeriod(
        permanent_id="PRD-00000001",
        label="Campagne présidentielle 2022",
        starts_at=date(2020, 1, 16),
        ends_at=date(2022, 4, 24),
    )

    repository = SimpleDocumentaryPeriodRepository(
        periods=(period,),
    )

    assert (
        repository.get_by_permanent_id(
            "PRD-00000001",
        )
        == period
    )
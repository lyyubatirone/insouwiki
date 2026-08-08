from datetime import date

from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)


DOCUMENTARY_PERIODS = (
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
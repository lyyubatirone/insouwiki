from dataclasses import dataclass
from typing import TypeAlias

from insouwiki.domain.documentary_date_range import (
    DocumentaryDateRange,
)


DocumentaryCriterionValue = (
    str
    | DocumentaryDateRange
)


@dataclass(frozen=True)
class DocumentaryCriterion:
    """
    Critère choisi par le lecteur pour préciser
    son exploration documentaire.
    """

    field: str
    value: DocumentaryCriterionValue
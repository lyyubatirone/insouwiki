from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class DocumentaryDateRange:
    """
    Intervalle de dates utilisé pour préciser
    une exploration documentaire.
    """

    start: date
    end: date
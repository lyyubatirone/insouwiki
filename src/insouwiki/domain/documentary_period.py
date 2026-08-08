from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class DocumentaryPeriod:
    """
    Période temporelle utilisée pour situer
    les documents dans leur contexte documentaire.
    """

    label: str
    starts_at: date
    ends_at: date | None = None
    permanent_id: str | None = None
    definition: str | None = None

    def contains(
        self,
        current_date: date,
    ) -> bool:
        if current_date < self.starts_at:
            return False

        if self.ends_at is None:
            return True

        return current_date <= self.ends_at
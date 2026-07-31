from dataclasses import dataclass
from datetime import date as Date


@dataclass(frozen=True)
class DocumentaryClue:
    """
    Piste documentaire proposée au lecteur
    à partir de son souvenir.
    """

    excerpt: str
    speaker: str | None = None
    contexte: str | None = None
    date: Date | None = None
    other_personalities: tuple[str, ...] = ()
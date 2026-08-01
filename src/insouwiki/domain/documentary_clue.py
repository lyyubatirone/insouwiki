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

from dataclasses import dataclass
from datetime import date as Date
from datetime import timedelta


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
    sequence_start: timedelta | None = None

from dataclasses import dataclass
from datetime import date as Date
from datetime import timedelta


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
    sequence_start: timedelta | None = None
    source_url: str | None = None

from dataclasses import dataclass
from datetime import date as Date
from datetime import timedelta


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
    sequence_start: timedelta | None = None
    sequence_end: timedelta | None = None
    source_url: str | None = None
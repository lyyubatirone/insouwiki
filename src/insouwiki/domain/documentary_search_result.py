from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass(frozen=True)
class DocumentarySearchResult:
    """
    Passage documentaire trouvé lors d'une recherche.
    """

    title: str
    author: str | None
    published_at: datetime | None
    sequence_text: str
    sequence_start: timedelta
    sequence_end: timedelta
    source_url: str
    query: str
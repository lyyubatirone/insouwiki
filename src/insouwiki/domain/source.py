from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl


class SourceStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"


class DocumentSourceRecord(BaseModel):
    """
    Source documentaire enregistrée dans le patrimoine documentaire.
    Exemple : une chaîne YouTube, un blog, un site web...
    """

    permanent_id: str | None = None

    source_kind: str

    name: str

    url: HttpUrl

    external_id: str

    status: SourceStatus = SourceStatus.ACTIVE

    first_discovered_at: datetime | None = None

    last_synchronized_at: datetime | None = None

    document_count: int = 0
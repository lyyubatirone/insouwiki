from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl

from insouwiki.domain.enums import (
    DocumentaryNature,
    DocumentKind,
    ProcessingStatus,
)


class Document(BaseModel):
    """
    Document documentaire découvert et enregistré par InsouWiki.
    """

    permanent_id: str | None = Field(default=None)

    source_permanent_id: str | None = None

    discovered_from_endpoint_permanent_id: str | None = None

    origin_key: str

    document_kind: DocumentKind

    title: str

    original_url: HttpUrl

    source_platform: str | None = None

    external_id: str | None = None

    author: str | None = None

    published_at: datetime | None = None

    thumbnail_url: HttpUrl | None = None

    documentary_nature: DocumentaryNature = DocumentaryNature.PRIMARY

    status: ProcessingStatus = ProcessingStatus.DISCOVERED
from datetime import datetime
from pydantic import BaseModel, Field

from insouwiki.domain.models import Document, DocumentSource


class DiscoveryReport(BaseModel):
    source: DocumentSource
    discovered_documents: list[Document] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
    started_at: datetime
    finished_at: datetime
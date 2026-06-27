from datetime import datetime
from pydantic import BaseModel, Field

from insouwiki.domain.document import Document
from insouwiki.domain.models import DiscoveryRequest

class DiscoveryReport(BaseModel):
    request: DiscoveryRequest
    discovered_documents: list[Document] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
    started_at: datetime
    finished_at: datetime
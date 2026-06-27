from datetime import datetime
from enum import Enum
from pydantic import BaseModel, HttpUrl, Field


class SourceKind(str, Enum):
    YOUTUBE_CHANNEL = "youtube_channel"
    YOUTUBE_VIDEO = "youtube_video"
    WEB_PAGE = "web_page"
    PDF = "pdf"
    AUDIO = "audio"
    VIDEO = "video"


class DocumentaryNature(str, Enum):
    PRIMARY = "primary"


class DocumentKind(str, Enum):
    VIDEO = "video"
    AUDIO = "audio"
    TEXT = "text"
    PDF = "pdf"
    WEB_PAGE = "web_page"


class ProcessingStatus(str, Enum):
    DISCOVERED = "discovered"
    REGISTERED = "registered"
    TRANSCRIBED = "transcribed"
    ANALYZED = "analyzed"
    PUBLISHED = "published"
    FAILED = "failed"


class DocumentSource(BaseModel):
    """
    Point d'entrée fourni par l'utilisateur.
    Exemple : une chaîne YouTube, une vidéo, un PDF, une page officielle.
    """

    source_kind: SourceKind
    url: HttpUrl
    documentary_nature: DocumentaryNature = DocumentaryNature.PRIMARY
    declared_author: str | None = None


class Document(BaseModel):
    """
    Document primaire découvert à partir d'une source.
    Exemple : une vidéo YouTube précise.
    """

    permanent_id: str | None = Field(
        default=None,
        description="Identifiant documentaire permanent, ex: SRC-00000001",
    )
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
from enum import Enum


class DiscoveryTargetKind(str, Enum):
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
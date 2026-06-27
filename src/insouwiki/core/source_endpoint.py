from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class Platform(StrEnum):
    """Plateforme ou canal de diffusion."""

    YOUTUBE = "youtube"
    WEBSITE = "website"
    RSS = "rss"
    PODCAST = "podcast"
    MASTODON = "mastodon"
    BLUESKY = "bluesky"


@dataclass(slots=True)
class SourceEndpoint:
    """Canal officiel de diffusion d'une source documentaire."""

    permanent_id: str
    source_permanent_id: str

    platform: Platform
    url: str
    canonical_url: str

    external_id: str | None = None
    status: str = "active"
    metadata: dict[str, Any] = field(default_factory=dict)
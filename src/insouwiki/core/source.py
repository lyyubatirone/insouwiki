from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class SourceKind(StrEnum):
    """Nature documentaire d'une source."""

    PERSON = "person"
    ORGANIZATION = "organization"
    INSTITUTION = "institution"
    PARTY = "party"
    THINK_TANK = "think_tank"
    ASSOCIATION = "association"


@dataclass(slots=True)
class Source:
    """Source documentaire."""

    permanent_id: str
    name: str
    kind: SourceKind
    status: str = "active"
    metadata: dict[str, Any] = field(default_factory=dict)
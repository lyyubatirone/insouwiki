from pydantic import BaseModel, HttpUrl

from insouwiki.domain.enums import (
    DiscoveryTargetKind,
    DocumentaryNature,
)


class DiscoveryRequest(BaseModel):
    """
    Point d'entrée fourni par l'utilisateur pour lancer une découverte.
    Exemple : une chaîne YouTube, une vidéo, un PDF, une page officielle.
    """

    source_kind: DiscoveryTargetKind

    url: HttpUrl

    documentary_nature: DocumentaryNature = DocumentaryNature.PRIMARY

    declared_author: str | None = None
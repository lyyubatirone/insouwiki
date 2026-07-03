from datetime import datetime, timedelta

from pydantic import BaseModel, HttpUrl


class DocumentaryPiece(BaseModel):
    """
    Pièce documentaire.

    Une pièce documentaire représente un élément du dossier
    documentaire présenté au lecteur afin qu'il puisse
    vérifier une affirmation à partir des sources primaires.

    Elle assemble les informations nécessaires à la lecture
    d'une séquence documentaire sans produire aucune
    interprétation.
    """

    permanent_id: str

    author: str

    document_title: str

    published_at: datetime | None = None

    sequence_text: str

    sequence_start: timedelta

    sequence_end: timedelta

    document_url: HttpUrl
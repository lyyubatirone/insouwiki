from pydantic import BaseModel


class DocumentaryEntity(BaseModel):
    """
    Entité documentaire.

    Une entité documentaire représente un objet du monde réel
    identifié de manière stable dans le patrimoine documentaire
    d'InsouWiki.

    Ses relations, fonctions, appartenances ou responsabilités
    ne font pas partie de son identité.
    """

    permanent_id: str

    entity_type: str

    name: str
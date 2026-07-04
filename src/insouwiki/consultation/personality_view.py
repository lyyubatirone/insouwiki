from pydantic import BaseModel


class PersonalityView(BaseModel):
    """
    Vue de consultation d'une personnalité.

    Cet objet contient uniquement les informations nécessaires
    à l'affichage d'une fiche personnalité.
    """

    name: str

    description: str

    document_count: int

    documentary_piece_count: int

    knowledge_count: int

    relation_count: int
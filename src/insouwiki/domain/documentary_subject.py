from pydantic import BaseModel


class DocumentarySubject(BaseModel):
    """
    Sujet documentaire.

    Représente un thème identifiable dans le patrimoine
    documentaire d'InsouWiki.
    """

    permanent_id: str

    label: str

    documentary_expressions: tuple[str, ...] = ()
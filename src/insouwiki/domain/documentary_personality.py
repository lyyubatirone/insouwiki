from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentaryPersonality:
    """
    Personnalité identifiée dans le patrimoine documentaire.
    """

    permanent_id: str
    slug: str
    display_name: str
    documentary_expressions: tuple[str, ...] = ()
    document_count: int = 0
from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentaryEvolution:
    """
    Première représentation d'une évolution documentaire.

    Cette version reste volontairement minimale.
    Elle sera enrichie progressivement au fil
    des prochains sprints.
    """

    permanent_id: str

    supporting_fact_ids: list[str]

    summary: str
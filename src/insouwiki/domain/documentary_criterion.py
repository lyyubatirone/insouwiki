from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentaryCriterion:
    """
    Critère choisi par le lecteur pour préciser
    son exploration documentaire.
    """

    field: str
    value: str
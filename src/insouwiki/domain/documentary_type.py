from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentaryType:
    """
    Nature documentaire d'une prise de parole.
    """

    label: str
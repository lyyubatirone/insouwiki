from dataclasses import dataclass


@dataclass(frozen=True)
class SequenceThemeAssociation:
    """
    Association entre une séquence documentaire
    et un thème documentaire.
    """

    sequence_id: str
    theme_id: str
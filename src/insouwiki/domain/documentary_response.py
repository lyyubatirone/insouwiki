from dataclasses import dataclass

from insouwiki.domain.documentary_clue import (
    DocumentaryClue,
)


@dataclass(frozen=True)
class DocumentaryResponse:
    """
    Réponse documentaire présentée au lecteur.

    Elle rassemble les pistes documentaires
    issues d'une exploration.
    """

    clues: tuple[DocumentaryClue, ...]

    def is_empty(self) -> bool:
        return len(self.clues) == 0

    def suggests_continuing_investigation(self) -> bool:
        return self.is_empty()
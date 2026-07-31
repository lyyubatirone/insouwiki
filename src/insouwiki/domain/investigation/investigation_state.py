from dataclasses import dataclass, replace


@dataclass(frozen=True)
class InvestigationState:
    """
    État d'une enquête documentaire.

    Cet objet représente ce qui peut être sauvegardé,
    partagé et repris ultérieurement.
    """

    question: str
    personalities: tuple[str, ...] = ()

    def with_personality(
        self,
        personality: str,
    ) -> "InvestigationState":
        if personality in self.personalities:
            return self

        return replace(
            self,
            personalities=(
                *self.personalities,
                personality,
            ),
        )
    
    def without_personality(
        self,
        personality: str,
    ) -> "InvestigationState":
        return replace(
            self,
            personalities=tuple(
                current_personality
                for current_personality in self.personalities
                if current_personality != personality
            ),
        )
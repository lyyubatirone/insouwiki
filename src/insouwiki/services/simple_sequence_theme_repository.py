from insouwiki.domain.sequence_theme_association import (
    SequenceThemeAssociation,
)
from insouwiki.domain.sequence_theme_repository import (
    SequenceThemeRepository,
)


class SimpleSequenceThemeRepository(
    SequenceThemeRepository,
):
    """
    Référentiel simple des associations
    entre séquences et thèmes.
    """

    def __init__(
        self,
        associations: tuple[
            SequenceThemeAssociation,
            ...
        ] = (),
    ):
        self.associations = associations

    def register(
        self,
        association: SequenceThemeAssociation,
    ) -> SequenceThemeAssociation:
        self.associations = (
            *self.associations,
            association,
        )

        return association

    def find_by_sequence(
        self,
        sequence_id: str,
    ) -> tuple[SequenceThemeAssociation, ...]:
        return tuple(
            association
            for association in self.associations
            if association.sequence_id == sequence_id
        )

    def find_by_theme(
        self,
        theme_id: str,
    ) -> tuple[SequenceThemeAssociation, ...]:
        return tuple(
            association
            for association in self.associations
            if association.theme_id == theme_id
        )
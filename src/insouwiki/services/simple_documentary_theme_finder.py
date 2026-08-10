from insouwiki.domain.documentary_sequence import (
    DocumentarySequence,
)
from insouwiki.domain.documentary_theme import (
    DocumentaryTheme,
)
from insouwiki.domain.documentary_theme_repository import (
    DocumentaryThemeRepository,
)
from insouwiki.domain.sequence_theme_repository import (
    SequenceThemeRepository,
)


class SimpleDocumentaryThemeFinder:
    """
    Retrouve les thèmes d'un document
    à partir de ses séquences.
    """

    def __init__(
        self,
        theme_repository: DocumentaryThemeRepository,
        association_repository: SequenceThemeRepository,
    ):
        self.theme_repository = theme_repository
        self.association_repository = association_repository

    def find_for_sequences(
        self,
        sequences: tuple[DocumentarySequence, ...],
    ) -> tuple[DocumentaryTheme, ...]:
        themes: list[DocumentaryTheme] = []
        seen_theme_ids: set[str] = set()

        for sequence in sequences:
            if sequence.permanent_id is None:
                continue

            associations = (
                self.association_repository.find_by_sequence(
                    sequence.permanent_id,
                )
            )

            for association in associations:
                if association.theme_id in seen_theme_ids:
                    continue

                theme = (
                    self.theme_repository.get_by_permanent_id(
                        association.theme_id,
                    )
                )

                if theme is None:
                    continue

                seen_theme_ids.add(
                    association.theme_id,
                )
                themes.append(theme)

        return tuple(themes)
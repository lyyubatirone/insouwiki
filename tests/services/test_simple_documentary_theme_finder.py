from datetime import timedelta

from insouwiki.domain.documentary_sequence import (
    DocumentarySequence,
)
from insouwiki.domain.documentary_theme import (
    DocumentaryTheme,
)
from insouwiki.domain.sequence_theme_association import (
    SequenceThemeAssociation,
)
from insouwiki.services.simple_documentary_theme_finder import (
    SimpleDocumentaryThemeFinder,
)
from insouwiki.services.simple_documentary_theme_repository import (
    SimpleDocumentaryThemeRepository,
)
from insouwiki.services.simple_sequence_theme_repository import (
    SimpleSequenceThemeRepository,
)


def test_finds_document_themes_from_sequences():
    sequences = (
        DocumentarySequence(
            permanent_id="SEQ-00000001",
            document_id="SRC-00000001",
            start=timedelta(seconds=0),
            end=timedelta(seconds=10),
            text="La retraite doit être à 60 ans.",
        ),
        DocumentarySequence(
            permanent_id="SEQ-00000002",
            document_id="SRC-00000001",
            start=timedelta(seconds=10),
            end=timedelta(seconds=20),
            text="Il faut renforcer la protection sociale.",
        ),
    )

    retirement = DocumentaryTheme(
        permanent_id="THM-00000001",
        label="Retraites",
    )

    social_protection = DocumentaryTheme(
        permanent_id="THM-00000002",
        label="Protection sociale",
    )

    theme_repository = SimpleDocumentaryThemeRepository(
        themes=(
            retirement,
            social_protection,
        ),
    )

    association_repository = SimpleSequenceThemeRepository(
        associations=(
            SequenceThemeAssociation(
                sequence_id="SEQ-00000001",
                theme_id="THM-00000001",
            ),
            SequenceThemeAssociation(
                sequence_id="SEQ-00000001",
                theme_id="THM-00000002",
            ),
            SequenceThemeAssociation(
                sequence_id="SEQ-00000002",
                theme_id="THM-00000002",
            ),
        ),
    )

    finder = SimpleDocumentaryThemeFinder(
        theme_repository=theme_repository,
        association_repository=association_repository,
    )

    themes = finder.find_for_sequences(
        sequences,
    )

    assert themes == (
        retirement,
        social_protection,
    )
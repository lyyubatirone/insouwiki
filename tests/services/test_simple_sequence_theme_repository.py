from insouwiki.domain.sequence_theme_association import (
    SequenceThemeAssociation,
)
from insouwiki.services.simple_sequence_theme_repository import (
    SimpleSequenceThemeRepository,
)


def test_finds_themes_associated_with_sequence():
    repository = SimpleSequenceThemeRepository()

    retirement = SequenceThemeAssociation(
        sequence_id="SEQ-00000001",
        theme_id="THM-00000001",
    )
    social_protection = SequenceThemeAssociation(
        sequence_id="SEQ-00000001",
        theme_id="THM-00000002",
    )
    ecology = SequenceThemeAssociation(
        sequence_id="SEQ-00000002",
        theme_id="THM-00000003",
    )

    repository.register(retirement)
    repository.register(social_protection)
    repository.register(ecology)

    assert repository.find_by_sequence(
        "SEQ-00000001",
    ) == (
        retirement,
        social_protection,
    )


def test_finds_sequences_associated_with_theme():
    repository = SimpleSequenceThemeRepository()

    first = SequenceThemeAssociation(
        sequence_id="SEQ-00000001",
        theme_id="THM-00000001",
    )
    second = SequenceThemeAssociation(
        sequence_id="SEQ-00000002",
        theme_id="THM-00000001",
    )
    other_theme = SequenceThemeAssociation(
        sequence_id="SEQ-00000003",
        theme_id="THM-00000002",
    )

    repository.register(first)
    repository.register(second)
    repository.register(other_theme)

    assert repository.find_by_theme(
        "THM-00000001",
    ) == (
        first,
        second,
    )
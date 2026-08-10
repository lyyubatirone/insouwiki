from insouwiki.domain.sequence_theme_association import (
    SequenceThemeAssociation,
)


def test_associates_documentary_sequence_with_theme():
    association = SequenceThemeAssociation(
        sequence_id="SEQ-00000001",
        theme_id="THM-00000001",
    )

    assert association.sequence_id == "SEQ-00000001"
    assert association.theme_id == "THM-00000001"
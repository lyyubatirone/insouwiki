from insouwiki.domain.documentary_subject_assignment import (
    DocumentarySubjectAssignment,
)


def test_assigns_subject_to_documentary_sequence():
    assignment = DocumentarySubjectAssignment(
        permanent_id="SAS-00000001",
        subject_id="SUB-00000001",
        sequence_id="SEQ-00000001",
    )

    assert assignment.subject_id == "SUB-00000001"
    assert assignment.sequence_id == "SEQ-00000001"
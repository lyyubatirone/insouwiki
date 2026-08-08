from insouwiki.domain.documentary_type import (
    DocumentaryType,
)


def test_creates_documentary_type():
    document_type = DocumentaryType(
        label="Interview",
    )

    assert document_type.label == "Interview"
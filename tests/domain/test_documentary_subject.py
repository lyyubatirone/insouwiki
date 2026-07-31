from insouwiki.domain.documentary_subject import (
    DocumentarySubject,
)


def test_creates_documentary_subject():
    subject = DocumentarySubject(
        permanent_id="SUB-00000001",
        label="Retraites",
    )

    assert subject.permanent_id == "SUB-00000001"
    assert subject.label == "Retraites"

def test_documentary_subject_keeps_documentary_expressions():
    subject = DocumentarySubject(
        permanent_id="SUB-00000001",
        label="Retraites",
        documentary_expressions=(
            "retraite",
            "retraites",
            "réforme des retraites",
        ),
    )

    assert subject.documentary_expressions == (
        "retraite",
        "retraites",
        "réforme des retraites",
    )
from datetime import timedelta

from insouwiki.domain.documentary_sequence import DocumentarySequence


def test_documentary_sequence_creation():
    sequence = DocumentarySequence(
        permanent_id="SEQ-00000001",
        document_id="DOC-00000001",
        start=timedelta(minutes=1, seconds=15),
        end=timedelta(minutes=1, seconds=42),
        text="Nous avons vécu un beau moment de notre histoire.",
    )

    assert sequence.permanent_id == "SEQ-00000001"
    assert sequence.document_id == "DOC-00000001"
    assert sequence.start == timedelta(minutes=1, seconds=15)
    assert sequence.end == timedelta(minutes=1, seconds=42)
    assert sequence.text == "Nous avons vécu un beau moment de notre histoire."
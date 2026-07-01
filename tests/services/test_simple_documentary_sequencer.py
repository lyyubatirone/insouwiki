from insouwiki.domain.document import Document
from insouwiki.domain.enums import DocumentKind
from insouwiki.domain.transcription import Transcription
from insouwiki.services.simple_documentary_sequencer import SimpleDocumentarySequencer


def test_simple_documentary_sequencer_creates_one_sequence():
    document = Document(
        permanent_id="DOC-00000001",
        origin_key="youtube:test-video",
        document_kind=DocumentKind.VIDEO,
        title="Vidéo de test",
        original_url="https://www.youtube.com/watch?v=test-video",
    )

    transcription = Transcription(
        document_id="DOC-00000001",
        language="fr",
        text="Nous avons vécu un beau moment de notre histoire.",
        engine="test",
    )

    sequencer = SimpleDocumentarySequencer()

    sequences = sequencer.sequence(
        document=document,
        transcription=transcription,
    )

    assert len(sequences) == 1

    sequence = sequences[0]

    assert sequence.permanent_id == "SEQ-00000001"
    assert sequence.document_id == "DOC-00000001"
    assert sequence.text == "Nous avons vécu un beau moment de notre histoire."
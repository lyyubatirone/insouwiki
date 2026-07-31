from datetime import timedelta

from insouwiki.domain.transcription import Transcription
from insouwiki.domain.transcription_segment import (
    TranscriptionSegment,
)
from insouwiki.services.simple_documentary_sequencer import (
    SimpleDocumentarySequencer,
)
from insouwiki.domain.document import Document
from insouwiki.domain.enums import DocumentKind


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

def test_groups_segments_from_same_reasoning():
    transcription = Transcription(
        permanent_id="TRS-00000001",
        document_id="SRC-00000001",
        language="fr",
        text=(
            "La retraite à 60 ans est une nécessité. "
            "Elle permet de protéger les travailleurs."
        ),
        engine="test",
        segments=[
            TranscriptionSegment(
                start=timedelta(seconds=0),
                end=timedelta(seconds=5),
                speaker="Jean-Luc Mélenchon",
                text=(
                    "La retraite à 60 ans "
                    "est une nécessité."
                ),
            ),
            TranscriptionSegment(
                start=timedelta(seconds=5),
                end=timedelta(seconds=10),
                speaker="Jean-Luc Mélenchon",
                text=(
                    "Elle permet de protéger "
                    "les travailleurs."
                ),
            ),
        ],
    )

    sequencer = SimpleDocumentarySequencer()

    sequences = sequencer.build_sequences(
        transcription,
    )

    assert len(sequences) == 1
    assert sequences[0].document_id == "SRC-00000001"
    assert sequences[0].start == timedelta(seconds=0)
    assert sequences[0].end == timedelta(seconds=10)
    assert sequences[0].text == (
        "La retraite à 60 ans est une nécessité.\n"
        "Elle permet de protéger les travailleurs."
    )
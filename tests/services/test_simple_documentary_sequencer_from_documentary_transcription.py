from datetime import timedelta

from insouwiki.domain.documentary_transcription import (
    DocumentaryTranscription,
)
from insouwiki.domain.transcription_segment import TranscriptionSegment
from insouwiki.services.simple_documentary_sequencer import (
    SimpleDocumentarySequencer,
)


def test_simple_documentary_sequencer_builds_one_sequence_from_one_segment():
    segment = TranscriptionSegment(
        start=timedelta(seconds=0),
        end=timedelta(seconds=5),
        speaker="Jean Dupont",
        text="Nous avons vécu un beau moment de notre histoire.",
    )

    transcription = DocumentaryTranscription(
        document_id="DOC-00000001",
        language="fr",
        segments=[segment],
    )

    sequencer = SimpleDocumentarySequencer()

    sequences = sequencer.build_sequences(transcription)

    assert len(sequences) == 1

    sequence = sequences[0]

    assert sequence.document_id == "DOC-00000001"
    assert sequence.start == timedelta(seconds=0)
    assert sequence.end == timedelta(seconds=5)
    assert sequence.text == "Nous avons vécu un beau moment de notre histoire."

def test_simple_documentary_sequencer_groups_segments_of_same_reasoning():
    first_segment = TranscriptionSegment(
        start=timedelta(seconds=0),
        end=timedelta(seconds=5),
        speaker="Jean Dupont",
        text="La retraite à 60 ans est une nécessité.",
    )

    second_segment = TranscriptionSegment(
        start=timedelta(seconds=5),
        end=timedelta(seconds=12),
        speaker="Jean Dupont",
        text="Elle permet à chacun de profiter de sa vie après le travail.",
    )

    transcription = DocumentaryTranscription(
        document_id="DOC-00000001",
        language="fr",
        segments=[
            first_segment,
            second_segment,
        ],
    )

    sequencer = SimpleDocumentarySequencer()

    sequences = sequencer.build_sequences(transcription)

    assert len(sequences) == 1

    sequence = sequences[0]

    assert sequence.document_id == "DOC-00000001"
    assert sequence.start == timedelta(seconds=0)
    assert sequence.end == timedelta(seconds=12)
    assert sequence.text == (
        "La retraite à 60 ans est une nécessité.\n"
        "Elle permet à chacun de profiter de sa vie après le travail."
    )

def test_simple_documentary_sequencer_splits_independent_reasonings():
    first_segment = TranscriptionSegment(
        start=timedelta(seconds=0),
        end=timedelta(seconds=5),
        speaker="Jean Dupont",
        text="La retraite à 60 ans est une nécessité sociale.",
    )

    second_segment = TranscriptionSegment(
        start=timedelta(seconds=5),
        end=timedelta(seconds=10),
        speaker="Jean Dupont",
        text="Passons maintenant à la planification écologique.",
    )

    transcription = DocumentaryTranscription(
        document_id="DOC-00000001",
        language="fr",
        segments=[
            first_segment,
            second_segment,
        ],
    )

    sequencer = SimpleDocumentarySequencer()

    sequences = sequencer.build_sequences(transcription)

    assert len(sequences) == 2

def test_simple_documentary_sequencer_keeps_question_and_answer_together():
    question = TranscriptionSegment(
        start=timedelta(seconds=0),
        end=timedelta(seconds=3),
        speaker="Journaliste",
        text="Pourquoi proposez-vous la retraite à 60 ans ?",
    )

    answer = TranscriptionSegment(
        start=timedelta(seconds=3),
        end=timedelta(seconds=12),
        speaker="Jean Dupont",
        text="Parce qu'elle permet à chacun de profiter de sa retraite en bonne santé.",
    )

    transcription = DocumentaryTranscription(
        document_id="DOC-00000001",
        language="fr",
        segments=[
            question,
            answer,
        ],
    )

    sequencer = SimpleDocumentarySequencer()

    sequences = sequencer.build_sequences(transcription)

    assert len(sequences) == 1

    sequence = sequences[0]

    assert sequence.start == timedelta(seconds=0)
    assert sequence.end == timedelta(seconds=12)
from datetime import timedelta

from insouwiki.domain.documentary_transcription import (
    DocumentaryTranscription,
)
from insouwiki.domain.transcription_segment import (
    TranscriptionSegment,
)


def test_documentary_transcription_holds_segments():
    segment = TranscriptionSegment(
        start=timedelta(seconds=0),
        end=timedelta(seconds=5),
        speaker="Jean Dupont",
        text="Bonjour à toutes et à tous.",
    )

    transcription = DocumentaryTranscription(
        document_id="DOC-000001",
        language="fr",
        segments=[segment],
    )

    assert transcription.document_id == "DOC-000001"
    assert transcription.language == "fr"
    assert len(transcription.segments) == 1
    assert transcription.segments[0].speaker == "Jean Dupont"
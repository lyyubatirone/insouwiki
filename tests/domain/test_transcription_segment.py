from datetime import timedelta

import pytest

from insouwiki.domain.transcription_segment import TranscriptionSegment


def test_transcription_segment_creation():
    segment = TranscriptionSegment(
        start=timedelta(seconds=12),
        end=timedelta(seconds=18),
        text="Nous sommes dans les locaux de la France insoumise.",
    )

    assert segment.start == timedelta(seconds=12)
    assert segment.end == timedelta(seconds=18)
    assert (
        segment.text
        == "Nous sommes dans les locaux de la France insoumise."
    )


def test_transcription_segment_end_cannot_precede_start():
    with pytest.raises(ValueError):
        TranscriptionSegment(
            start=timedelta(seconds=20),
            end=timedelta(seconds=10),
            text="Segment invalide",
        )
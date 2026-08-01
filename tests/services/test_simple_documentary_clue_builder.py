from datetime import datetime, date, timedelta

from insouwiki.domain.documentary_search_result import (
    DocumentarySearchResult,
)
from insouwiki.services.simple_documentary_clue_builder import (
    SimpleDocumentaryClueBuilder,
)


def test_builds_documentary_clue_from_search_result():
    result = DocumentarySearchResult(
        title="France Inter",
        author="Jean-Luc Mélenchon",
        published_at=datetime(2022, 4, 12),
        sequence_text="La retraite doit être à 60 ans.",
        sequence_start=timedelta(minutes=3, seconds=17),
        sequence_end=timedelta(minutes=3, seconds=42),
        source_url="https://example.com",
        query="60 ans",
    )

    builder = SimpleDocumentaryClueBuilder()

    clue = builder.build(result)

    assert clue.excerpt == "La retraite doit être à 60 ans."
    assert clue.speaker == "Jean-Luc Mélenchon"
    assert clue.date == date(2022, 4, 12)

def test_builds_documentary_clue_when_metadata_is_unknown():
    result = DocumentarySearchResult(
        title="Document sans métadonnées complètes",
        author=None,
        published_at=None,
        sequence_text="Passage documentaire retrouvé.",
        sequence_start=timedelta(seconds=10),
        sequence_end=timedelta(seconds=20),
        source_url="https://example.com",
        query="passage retrouvé",
    )

    builder = SimpleDocumentaryClueBuilder()

    clue = builder.build(result)

    assert clue.excerpt == "Passage documentaire retrouvé."
    assert clue.speaker is None
    assert clue.date is None

from datetime import date as Date
from datetime import datetime, timedelta


def test_builds_documentary_clue_with_sequence_start():
    result = DocumentarySearchResult(
        title="France Inter",
        author="Jean-Luc Mélenchon",
        published_at=datetime(2022, 4, 12),
        sequence_text="La retraite doit être à 60 ans.",
        sequence_start=timedelta(minutes=3, seconds=17),
        sequence_end=timedelta(minutes=3, seconds=42),
        source_url="https://example.com",
        query="60 ans",
    )

    builder = SimpleDocumentaryClueBuilder()

    clue = builder.build(result)

    assert clue.sequence_start == timedelta(
        minutes=3,
        seconds=17,
    )

def test_builds_documentary_clue_with_source_url():
    result = DocumentarySearchResult(
        title="France Inter",
        author="Jean-Luc Mélenchon",
        published_at=datetime(2022, 4, 12),
        sequence_text="La retraite doit être à 60 ans.",
        sequence_start=timedelta(minutes=3, seconds=17),
        sequence_end=timedelta(minutes=3, seconds=42),
        source_url="https://example.com/watch?v=123&t=197",
        query="60 ans",
    )

    builder = SimpleDocumentaryClueBuilder()

    clue = builder.build(result)

    assert clue.source_url == (
        "https://example.com/watch?v=123&t=197"
    )

def test_builds_documentary_clue_with_sequence_end():
    result = DocumentarySearchResult(
        title="France Inter",
        author="Jean-Luc Mélenchon",
        published_at=datetime(2022, 4, 12),
        sequence_text="La retraite doit être à 60 ans.",
        sequence_start=timedelta(minutes=3, seconds=17),
        sequence_end=timedelta(minutes=3, seconds=42),
        source_url="https://example.com/watch?v=123&t=197",
        query="60 ans",
    )

    builder = SimpleDocumentaryClueBuilder()

    clue = builder.build(result)

    assert clue.sequence_end == timedelta(
        minutes=3,
        seconds=42,
    )
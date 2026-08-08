from datetime import timedelta

from fastapi.testclient import TestClient

from insouwiki.consultation.documentary_library import (
    DocumentaryLibrary,
)
from insouwiki.domain.transcription import (
    Transcription,
)
from insouwiki.domain.transcription_segment import (
    TranscriptionSegment,
)
from insouwiki.web.app import app
from insouwiki.web.routes.document import (
    get_documentary_library,
)


client = TestClient(app)


class InMemoryTranscriptionRepository:
    def __init__(
        self,
        transcriptions: list[Transcription],
    ):
        self.transcriptions = transcriptions

    def find_by_document(
        self,
        document_permanent_id: str,
    ) -> Transcription | None:
        for transcription in self.transcriptions:
            if (
                transcription.document_id
                == document_permanent_id
            ):
                return transcription

        return None


def test_can_open_document_page():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert response.status_code == 200


def test_document_page_displays_title():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert (
        "Clip officiel de Jean-Luc Mélenchon"
        in response.text
    )

def test_document_page_displays_author():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "JEAN-LUC MÉLENCHON" in response.text


def test_document_page_displays_source_platform():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "YouTube" in response.text


def test_document_page_links_to_original_source():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "youtube.com" in response.text


def test_document_page_displays_publication_date():
    response = client.get(
        "/documents/SRC-00003151",
    )

    assert "2015" in response.text


def test_document_page_displays_transcription_section():
    response = client.get(
        "/documents/SRC-00003151",
    )

    assert "Transcription" in response.text


def test_document_page_indicates_missing_transcription():
    response = client.get(
        "/documents/SRC-00003151",
    )

    assert (
        "Aucune transcription disponible."
        in response.text
    )


def test_document_page_displays_existing_transcription():
    transcription = Transcription(
        permanent_id="TRS-00000001",
        document_id="SRC-00000001",
        language="fr",
        text="Bonjour à toutes et à tous.",
        engine="test",
    )

    test_library = DocumentaryLibrary(
        transcription_repository=(
            InMemoryTranscriptionRepository(
                [transcription],
            )
        ),
    )

    app.dependency_overrides[
        get_documentary_library
    ] = lambda: test_library

    try:
        response = client.get(
            "/documents/SRC-00000001",
        )

        assert response.status_code == 200
        assert (
            "Bonjour à toutes et à tous."
            in response.text
        )
        assert (
            "Aucune transcription disponible."
            not in response.text
        )
    finally:
        app.dependency_overrides.clear()


def test_document_page_displays_transcription_segments():
    transcription = Transcription(
        permanent_id="TRS-00000001",
        document_id="SRC-00000001",
        language="fr",
        text=(
            "Bonjour à toutes et à tous. "
            "Je voudrais vous parler "
            "de la retraite à 60 ans."
        ),
        engine="test",
        segments=[
            TranscriptionSegment(
                start=timedelta(seconds=0),
                end=timedelta(seconds=5),
                speaker="Jean-Luc Mélenchon",
                text="Bonjour à toutes et à tous.",
            ),
            TranscriptionSegment(
                start=timedelta(seconds=5),
                end=timedelta(seconds=12),
                speaker="Jean-Luc Mélenchon",
                text=(
                    "Je voudrais vous parler "
                    "de la retraite à 60 ans."
                ),
            ),
        ],
    )

    test_library = DocumentaryLibrary(
        transcription_repository=(
            InMemoryTranscriptionRepository(
                [transcription],
            )
        ),
    )

    app.dependency_overrides[
        get_documentary_library
    ] = lambda: test_library

    try:
        response = client.get(
            "/documents/SRC-00000001",
        )

        assert response.status_code == 200
        assert (
            "Bonjour à toutes et à tous."
            in response.text
        )
        assert (
            "Je voudrais vous parler "
            "de la retraite à 60 ans."
            in response.text
        )
    finally:
        app.dependency_overrides.clear()

def test_transcription_segments_are_displayed_individually():
    transcription = Transcription(
        permanent_id="TRS-00000001",
        document_id="SRC-00000001",
        language="fr",
        text=(
            "Bonjour à toutes et à tous. "
            "Je voudrais vous parler "
            "de la retraite à 60 ans."
        ),
        engine="test",
        segments=[
            TranscriptionSegment(
                start=timedelta(seconds=0),
                end=timedelta(seconds=5),
                speaker="Jean-Luc Mélenchon",
                text="Bonjour à toutes et à tous.",
            ),
            TranscriptionSegment(
                start=timedelta(seconds=5),
                end=timedelta(seconds=12),
                speaker="Jean-Luc Mélenchon",
                text=(
                    "Je voudrais vous parler "
                    "de la retraite à 60 ans."
                ),
            ),
        ],
    )

    test_library = DocumentaryLibrary(
        transcription_repository=(
            InMemoryTranscriptionRepository(
                [transcription],
            )
        ),
    )

    app.dependency_overrides[
        get_documentary_library
    ] = lambda: test_library

    try:
        response = client.get(
            "/documents/SRC-00000001",
        )

        assert (
            response.text.count(
                'class="transcription-segment"'
            )
            == 2
        )
    finally:
        app.dependency_overrides.clear()

def test_document_page_displays_documentary_sequences():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "Séquences documentaires" in response.text
    assert (
        "Séquence documentaire de test."
        in response.text
    )

def test_documentary_piece_links_to_video_passage():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert (
        "Voir ce passage dans la vidéo"
        in response.text
    )
    assert "t=0s" in response.text

def test_document_page_displays_documentary_facts():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "Faits documentaires" in response.text

def test_document_page_displays_documentary_notice():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "Notice documentaire" in response.text

def test_documentary_summary_displays_document_title():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "Document :" in response.text

def test_document_page_displays_documentary_fact_author():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert (
        '<li class="documentary-fact">'
        in response.text
    )

    assert "<strong>" in response.text

def test_document_page_displays_fact_source():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "Source documentaire" in response.text

def test_document_page_displays_fact_source_time_range():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "Source documentaire" in response.text
    assert "0:00:10" in response.text
    assert "0:00:20" in response.text

def test_document_page_links_fact_to_source_passage():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "t=10s" in response.text
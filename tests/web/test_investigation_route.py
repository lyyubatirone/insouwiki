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

def test_route_accepts_multiple_personalities():
    response = client.get(
        "/enquetes",
        params=[
            ("q", "Corse"),
            ("personality", "Jean-Luc Mélenchon"),
            ("personality", "Manuel Bompard"),
        ],
    )

    assert response.status_code == 200

def test_route_displays_multiple_selected_personalities():
    response = client.get(
        "/enquetes",
        params=[
            ("q", "Corse"),
            ("personality", "Jean-Luc Mélenchon"),
            ("personality", "Manuel Bompard"),
        ],
    )

    assert response.status_code == 200
    assert "Jean-Luc Mélenchon" in response.text
    assert "Manuel Bompard" in response.text

def test_selected_personalities_are_displayed_as_active_filters():
    response = client.get(
        "/enquetes",
        params=[
            ("q", "Corse"),
            ("personality", "Jean-Luc Mélenchon"),
            ("personality", "Manuel Bompard"),
        ],
    )

    assert 'class="active-filters"' in response.text
    assert response.text.count(
        'class="active-filter"'
    ) == 2

def test_remove_symbol_is_a_link():
    response = client.get(
        "/enquetes",
        params=[
            ("q", "Corse"),
            ("personality", "Jean-Luc Mélenchon"),
            ("personality", "Manuel Bompard"),
        ],
    )

    assert '<a' in response.text

def test_remove_link_removes_personality_from_url():
    response = client.get(
        "/enquetes",
        params=[
            ("q", "Corse"),
            ("personality", "Jean-Luc Mélenchon"),
            ("personality", "Manuel Bompard"),
        ],
    )

    assert "Manuel+Bompard" in response.text
    assert 'aria-label="Retirer Jean-Luc Mélenchon"' in response.text

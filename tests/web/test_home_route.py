from fastapi.testclient import TestClient

from insouwiki.web.app import app


client = TestClient(app)


def test_home_links_to_personality_catalog():
    response = client.get("/")

    assert response.status_code == 200
    assert "/personnalites" in response.text

def test_document_page_displays_fact_author():
    response = client.get(
        "/documents/SRC-00000001",
    )

    assert "Jean-Luc Mélenchon" in response.text
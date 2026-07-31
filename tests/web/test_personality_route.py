from fastapi.testclient import TestClient

from insouwiki.web.app import app


client = TestClient(app)


def test_lists_all_documentary_personalities():
    response = client.get(
        "/personnalites",
    )

    assert response.status_code == 200
    assert "JEAN-LUC MÉLENCHON" in response.text
    assert "Manuel Bompard" in response.text

def test_personality_page_lists_documents():
    response = client.get(
        "/personnalites/jean-luc-melenchon",
    )

    assert "<h2>Documents</h2>" in response.text
    assert "/documents/" in response.text
from insouwiki.domain.documentary_personality import (
    DocumentaryPersonality,
)
from insouwiki.services.simple_documentary_personality_repository import (
    SimpleDocumentaryPersonalityRepository,
)
from insouwiki.domain.document import Document

def test_lists_no_personality_without_documents():
    repository = SimpleDocumentaryPersonalityRepository()

    personalities = repository.list_all()

    assert personalities == []

def test_discovers_distinct_personalities_from_documents():
    documents = [
        Document(
            origin_key="1",
            document_kind="video",
            title="Discours 1",
            original_url="https://a",
            author="Jean-Luc Mélenchon",
        ),
        Document(
            origin_key="2",
            document_kind="video",
            title="Discours 2",
            original_url="https://b",
            author="Jean-Luc Mélenchon",
        ),
    ]

    repository = SimpleDocumentaryPersonalityRepository(
        documents,
    )

    personalities = repository.list_all()

    assert len(personalities) == 1
    assert personalities[0].display_name == (
        "Jean-Luc Mélenchon"
    )

def test_counts_documents_per_personality():
    documents = [
        Document(
            origin_key="1",
            document_kind="video",
            title="Discours 1",
            original_url="https://a",
            author="Jean-Luc Mélenchon",
        ),
        Document(
            origin_key="2",
            document_kind="video",
            title="Discours 2",
            original_url="https://b",
            author="Jean-Luc Mélenchon",
        ),
        Document(
            origin_key="3",
            document_kind="video",
            title="Discours 3",
            original_url="https://c",
            author="Manuel Bompard",
        ),
    ]

    repository = SimpleDocumentaryPersonalityRepository(
        documents,
    )

    personalities = repository.list_all()

    assert personalities[0].document_count == 2
    assert personalities[1].document_count == 1
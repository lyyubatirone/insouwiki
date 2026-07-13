from insouwiki.domain.document import Document
from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.enums import DocumentKind
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)
from insouwiki.services.in_memory_documentary_repository import (
    InMemoryDocumentaryRepository,
)


def build_document(
    origin_key: str,
    title: str,
    author: str,
) -> Document:
    return Document(
        origin_key=origin_key,
        document_kind=DocumentKind.VIDEO,
        title=title,
        original_url=(
            "https://www.youtube.com/watch"
            f"?v={origin_key}"
        ),
        author=author,
    )


def test_repository_returns_all_documents():
    melenchon_document = build_document(
        origin_key="melenchon-discours",
        title="Discours",
        author="Jean-Luc Mélenchon",
    )

    bardella_document = build_document(
        origin_key="bardella-interview",
        title="Interview",
        author="Jordan Bardella",
    )

    repository = InMemoryDocumentaryRepository(
        documents=(
            melenchon_document,
            bardella_document,
        ),
    )

    exploration = DocumentaryExploration(
        intent=ExplorationIntent.UNDERSTAND,
        question=DocumentaryQuestion(
            text="Retraites",
        ),
        criteria=(),
        subjects=[],
        observations=[],
    )

    inventory = repository.explore(
        exploration,
    )

    assert inventory.documents == (
        melenchon_document,
        bardella_document,
    )


def test_repository_filters_documents_by_author():
    melenchon_document = build_document(
        origin_key="melenchon-discours",
        title="Discours",
        author="Jean-Luc Mélenchon",
    )

    bardella_document = build_document(
        origin_key="bardella-interview",
        title="Interview",
        author="Jordan Bardella",
    )

    repository = InMemoryDocumentaryRepository(
        documents=(
            melenchon_document,
            bardella_document,
        ),
    )

    exploration = DocumentaryExploration(
        intent=ExplorationIntent.UNDERSTAND,
        question=DocumentaryQuestion(
            text="Retraites",
        ),
        criteria=(
            DocumentaryCriterion(
                field="auteur",
                value="Jean-Luc Mélenchon",
            ),
        ),
        subjects=[],
        observations=[],
    )

    inventory = repository.explore(
        exploration,
    )

    assert inventory.documents == (
        melenchon_document,
    )
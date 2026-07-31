from datetime import datetime
from datetime import date

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
from insouwiki.registry import repository
from insouwiki.services.in_memory_documentary_repository import (
    InMemoryDocumentaryRepository,
)
from insouwiki.domain.documentary_date_range import (
    DocumentaryDateRange,
)
from insouwiki.domain.documentary_request import (
    DocumentaryRequest,
)

def build_document(
    origin_key: str,
    title: str,
    author: str,
    published_at: datetime | None = None,
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
        published_at=published_at,
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

    inventory = exploration.explore(
        repository,
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

def test_repository_filters_documents_by_date_range():
    melenchon_2021 = build_document(
        origin_key="melenchon-2021",
        title="Discours 2021",
        author="Jean-Luc Mélenchon",
        published_at=datetime(2021, 5, 15),
    )

    melenchon_2023 = build_document(
        origin_key="melenchon-2023",
        title="Discours 2023",
        author="Jean-Luc Mélenchon",
        published_at=datetime(2023, 3, 10),
    )

    bardella_2023 = build_document(
        origin_key="bardella-2023",
        title="Discours 2023",
        author="Jordan Bardella",
        published_at=datetime(2023, 4, 20),
    )

    repository = InMemoryDocumentaryRepository(
        documents=(
            melenchon_2021,
            melenchon_2023,
            bardella_2023,
        ),
    )

    exploration = DocumentaryExploration(
        intent=ExplorationIntent.UNDERSTAND,
        question=DocumentaryQuestion(
            text="Retraites",
        ),
        criteria=(
            DocumentaryCriterion(
                field="published_at",
                value=DocumentaryDateRange(
                    start=date(2022, 1, 1),
                    end=date(2023, 12, 31),
                ),
            ),
        ),
        subjects=[],
        observations=[],
    )

    inventory = repository.explore(
        exploration,
    )

    assert inventory.documents == (
        melenchon_2023,
        bardella_2023,
    )

    """
    Premier scénario complet d'exploration documentaire.

    Le lecteur affine progressivement son exploration
    jusqu'à obtenir le document recherché.
    """

def test_reader_can_refine_a_documentary_exploration():
    melenchon_2021 = build_document(
        origin_key="melenchon-2021",
        title="Discours 2021",
        author="Jean-Luc Mélenchon",
        published_at=datetime(2021, 5, 15),
    )

    melenchon_2023 = build_document(
        origin_key="melenchon-2023",
        title="Discours 2023",
        author="Jean-Luc Mélenchon",
        published_at=datetime(2023, 3, 10),
    )

    bardella_2023 = build_document(
        origin_key="bardella-2023",
        title="Interview 2023",
        author="Jordan Bardella",
        published_at=datetime(2023, 4, 20),
    )

    repository = InMemoryDocumentaryRepository(
        documents=(
            melenchon_2021,
            melenchon_2023,
            bardella_2023,
        ),
    )

    request = DocumentaryRequest(
        text="Retraites",
    )

    exploration = request.start()

    exploration = exploration.refine(
        DocumentaryCriterion(
            field="auteur",
            value="Jean-Luc Mélenchon",
        ),
    )

    exploration = exploration.refine(
        DocumentaryCriterion(
            field="published_at",
            value=DocumentaryDateRange(
                start=date(2022, 1, 1),
                end=date(2023, 12, 31),
            ),
        ),
    )

    inventory = repository.explore(
        exploration,
    )

    assert inventory.documents == (
        melenchon_2023,
    )
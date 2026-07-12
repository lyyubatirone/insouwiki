from datetime import timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_inventory import (
    DocumentaryInventory,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.documentary_sequence import (
    DocumentarySequence,
)
from insouwiki.domain.enums import DocumentKind
from insouwiki.services.documentary_inventory_service import (
    DocumentaryInventoryService,
)


class FakeDocumentRepository:
    def __init__(
        self,
        documents: list[Document],
    ) -> None:
        self._documents = {
            document.permanent_id: document
            for document in documents
        }

    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> Document | None:
        return self._documents.get(permanent_id)


class FakeSequenceRepository:
    def __init__(
        self,
        sequences: list[DocumentarySequence],
    ) -> None:
        self._sequences = sequences
        self.received_query: str | None = None

    def search(
        self,
        query: str,
    ) -> list[DocumentarySequence]:
        self.received_query = query
        return self._sequences


def build_document(
    permanent_id: str,
    title: str,
) -> Document:
    return Document(
        permanent_id=permanent_id,
        origin_key=f"youtube:{permanent_id}",
        document_kind=DocumentKind.VIDEO,
        title=title,
        original_url=(
            f"https://www.youtube.com/watch?v={permanent_id}"
        ),
    )


def build_sequence(
    permanent_id: str,
    document_id: str,
    text: str,
) -> DocumentarySequence:
    return DocumentarySequence(
        permanent_id=permanent_id,
        document_id=document_id,
        start=timedelta(seconds=0),
        end=timedelta(seconds=5),
        text=text,
    )


def test_builds_inventory_without_duplicate_documents():
    first_document = build_document(
        permanent_id="SRC-00000001",
        title="Premier document",
    )
    second_document = build_document(
        permanent_id="SRC-00000002",
        title="Deuxième document",
    )

    sequence_repository = FakeSequenceRepository(
        sequences=[
            build_sequence(
                permanent_id="SEQ-00000001",
                document_id="SRC-00000001",
                text="La retraite à 60 ans.",
            ),
            build_sequence(
                permanent_id="SEQ-00000002",
                document_id="SRC-00000001",
                text="Nous défendons cette mesure.",
            ),
            build_sequence(
                permanent_id="SEQ-00000003",
                document_id="SRC-00000002",
                text="La retraite à 60 ans est nécessaire.",
            ),
        ]
    )

    service = DocumentaryInventoryService(
        document_repository=FakeDocumentRepository(
            documents=[
                first_document,
                second_document,
            ]
        ),
        sequence_repository=sequence_repository,
    )

    question = DocumentaryQuestion(
        text="retraite à 60 ans",
    )

    inventory = service.build(question)

    assert isinstance(inventory, DocumentaryInventory)
    assert inventory.documents == (
        first_document,
        second_document,
    )
    assert inventory.document_count == 2
    assert sequence_repository.received_query == question.text
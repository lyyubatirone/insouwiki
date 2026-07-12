from insouwiki.domain.document import Document
from insouwiki.domain.documentary_inventory import (
    DocumentaryInventory,
)
from insouwiki.domain.enums import DocumentKind


def build_document(
    origin_key: str,
    title: str,
) -> Document:
    return Document(
        origin_key=origin_key,
        document_kind=DocumentKind.VIDEO,
        title=title,
        original_url=f"https://example.com/{origin_key}",
    )


def test_inventory_keeps_all_documents():
    first = build_document(
        origin_key="doc-1",
        title="Premier document",
    )

    second = build_document(
        origin_key="doc-2",
        title="Deuxième document",
    )

    inventory = DocumentaryInventory(
        documents=[
            first,
            second,
        ]
    )

    assert inventory.documents == [
        first,
        second,
    ]


def test_inventory_knows_document_count():
    inventory = DocumentaryInventory(
        documents=[
            build_document(
                origin_key="doc-1",
                title="Premier document",
            ),
            build_document(
                origin_key="doc-2",
                title="Deuxième document",
            ),
        ]
    )

    assert inventory.document_count == 2

def test_inventory_can_be_empty():
    inventory = DocumentaryInventory()

    assert inventory.documents == ()
    assert inventory.document_count == 0
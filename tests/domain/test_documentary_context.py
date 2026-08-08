from insouwiki.domain.documentary_context import (
    DocumentaryContext,
)


def test_creates_documentary_context():
    context = DocumentaryContext(
        label="Campagne présidentielle 2022",
    )

    assert context.label == "Campagne présidentielle 2022"
from insouwiki.services.document_availability_analyzer import (
    DocumentAvailabilityAnalyzer,
)


def test_detects_unavailable_documents():
    analyzer = DocumentAvailabilityAnalyzer()

    previous_documents = {
        "youtube:A",
        "youtube:B",
        "youtube:C",
    }

    current_documents = {
        "youtube:A",
        "youtube:B",
    }

    unavailable = analyzer.detect_unavailable_documents(
        previous_documents=previous_documents,
        current_documents=current_documents,
    )

    assert unavailable == {"youtube:C"}
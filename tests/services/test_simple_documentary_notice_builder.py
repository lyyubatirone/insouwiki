from datetime import date, datetime

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)
from insouwiki.services.simple_documentary_notice_builder import (
    SimpleDocumentaryNoticeBuilder,
)
from insouwiki.services.simple_documentary_period_finder import (
    SimpleDocumentaryPeriodFinder,
)
from insouwiki.domain.documentary_notice import (
    DocumentaryNotice,
)

class InMemoryDocumentaryPeriodRepository:
    def __init__(
        self,
        periods: tuple[DocumentaryPeriod, ...],
    ):
        self.periods = periods

    def list_all(
        self,
    ) -> tuple[DocumentaryPeriod, ...]:
        return self.periods

def test_builds_empty_documentary_notice():
    builder = SimpleDocumentaryNoticeBuilder()

    document = Document(
    permanent_id="SRC-00000001",
    origin_key="test-document",
    title="Document de test",
    document_kind="video",
    original_url="https://example.com/document",
)

    notice = builder.build(document)

    assert notice == DocumentaryNotice()

from datetime import date, datetime

from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)
from insouwiki.services.simple_documentary_period_finder import (
    SimpleDocumentaryPeriodFinder,
)


def test_builds_notice_with_documentary_contexts():
    periods = (
        DocumentaryPeriod(
            label="Mandat présidentiel 2017–2022",
            starts_at=date(2017, 5, 14),
            ends_at=date(2022, 5, 13),
        ),
        DocumentaryPeriod(
            label="Campagne présidentielle 2022",
            starts_at=date(2022, 3, 7),
            ends_at=date(2022, 4, 24),
        ),
        DocumentaryPeriod(
            label="XVe législature (2017–2022)",
            starts_at=date(2017, 6, 21),
            ends_at=date(2022, 6, 21),
        ),
    )

    repository = InMemoryDocumentaryPeriodRepository(
        periods,
    )

    finder = SimpleDocumentaryPeriodFinder(
        repository=repository,
    )

    builder = SimpleDocumentaryNoticeBuilder(
        period_finder=finder,
    )

    document = Document(
        permanent_id="SRC-00000001",
        origin_key="test-document",
        title="Document de test",
        document_kind="video",
        original_url="https://example.com/document",
        published_at=datetime(
            2022,
            4,
            12,
            12,
            0,
        ),
    )

    repository = InMemoryDocumentaryPeriodRepository(
        periods,
    )

    finder = SimpleDocumentaryPeriodFinder(
        repository=repository,
    )
    notice = builder.build(document)

    assert notice.documentary_contexts == (
        "Mandat présidentiel 2017–2022",
        "Campagne présidentielle 2022",
        "XVe législature (2017–2022)",
    )

def test_builds_notice_without_context_when_publication_date_is_unknown():
    periods = (
        DocumentaryPeriod(
            label="Campagne présidentielle 2022",
            starts_at=date(2022, 3, 7),
            ends_at=date(2022, 4, 24),
        ),
    )

    repository = InMemoryDocumentaryPeriodRepository(
        periods,
    )

    finder = SimpleDocumentaryPeriodFinder(
        repository=repository,
    )

    builder = SimpleDocumentaryNoticeBuilder(
        period_finder=finder,
    )

    document = Document(
        permanent_id="SRC-00000001",
        origin_key="test-document",
        title="Document de test",
        document_kind="video",
        original_url="https://example.com/document",
        published_at=None,
    )

    repository = InMemoryDocumentaryPeriodRepository(
        periods,
    )

    finder = SimpleDocumentaryPeriodFinder(
        repository=repository,
    )

    notice = builder.build(document)

    assert notice.documentary_contexts == ()

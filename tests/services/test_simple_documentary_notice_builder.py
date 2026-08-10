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
from datetime import date, datetime, timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)
from insouwiki.domain.documentary_sequence import (
    DocumentarySequence,
)
from insouwiki.domain.documentary_theme import (
    DocumentaryTheme,
)
from insouwiki.domain.sequence_theme_association import (
    SequenceThemeAssociation,
)
from insouwiki.services.simple_documentary_theme_finder import (
    SimpleDocumentaryThemeFinder,
)
from insouwiki.services.simple_documentary_theme_repository import (
    SimpleDocumentaryThemeRepository,
)
from insouwiki.services.simple_sequence_theme_repository import (
    SimpleSequenceThemeRepository,
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

def test_builds_notice_with_contexts_and_themes():
    periods = (
        DocumentaryPeriod(
            permanent_id="PRD-00000001",
            label="Campagne présidentielle 2022",
            starts_at=date(2020, 1, 16),
            ends_at=date(2022, 4, 24),
        ),
    )

    period_repository = InMemoryDocumentaryPeriodRepository(
        periods,
    )

    period_finder = SimpleDocumentaryPeriodFinder(
        repository=period_repository,
    )

    retirement = DocumentaryTheme(
        permanent_id="THM-00000001",
        label="Retraites",
    )

    social_protection = DocumentaryTheme(
        permanent_id="THM-00000002",
        label="Protection sociale",
    )

    theme_repository = SimpleDocumentaryThemeRepository(
        themes=(
            retirement,
            social_protection,
        ),
    )

    association_repository = SimpleSequenceThemeRepository(
        associations=(
            SequenceThemeAssociation(
                sequence_id="SEQ-00000001",
                theme_id="THM-00000001",
            ),
            SequenceThemeAssociation(
                sequence_id="SEQ-00000002",
                theme_id="THM-00000002",
            ),
        ),
    )

    theme_finder = SimpleDocumentaryThemeFinder(
        theme_repository=theme_repository,
        association_repository=association_repository,
    )

    builder = SimpleDocumentaryNoticeBuilder(
        period_finder=period_finder,
        theme_finder=theme_finder,
    )

    document = Document(
        permanent_id="SRC-00000001",
        origin_key="test-document",
        document_kind="video",
        title="Document de test",
        original_url="https://example.com/document",
        published_at=datetime(
            2022,
            3,
            29,
            12,
            0,
        ),
    )

    sequences = (
        DocumentarySequence(
            permanent_id="SEQ-00000001",
            document_id="SRC-00000001",
            start=timedelta(seconds=0),
            end=timedelta(seconds=10),
            text="La retraite doit être à 60 ans.",
        ),
        DocumentarySequence(
            permanent_id="SEQ-00000002",
            document_id="SRC-00000001",
            start=timedelta(seconds=10),
            end=timedelta(seconds=20),
            text="Il faut renforcer la protection sociale.",
        ),
    )

    notice = builder.build(
        document,
        sequences=sequences,
    )

    assert notice.documentary_contexts == (
        "Campagne présidentielle 2022",
    )

    assert notice.themes == (
        "Retraites",
        "Protection sociale",
    )

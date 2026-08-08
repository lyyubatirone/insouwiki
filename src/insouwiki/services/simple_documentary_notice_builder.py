from insouwiki.domain.document import Document
from insouwiki.domain.documentary_notice import (
    DocumentaryNotice,
)
from insouwiki.services.simple_documentary_period_finder import (
    SimpleDocumentaryPeriodFinder,
)


class SimpleDocumentaryNoticeBuilder:
    """Construit une notice documentaire."""

    def __init__(
        self,
        period_finder: SimpleDocumentaryPeriodFinder | None = None,
    ):
        self.period_finder = period_finder

    def build(
        self,
        document: Document,
    ) -> DocumentaryNotice:
        if (
            self.period_finder is None
            or document.published_at is None
        ):
            return DocumentaryNotice()

        periods = self.period_finder.find_all_for(
            document.published_at.date(),
        )

        return DocumentaryNotice(
            documentary_contexts=tuple(
                period.label
                for period in periods
            ),
        )
    
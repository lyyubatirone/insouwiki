from insouwiki.domain.document import Document
from insouwiki.domain.documentary_notice import (
    DocumentaryNotice,
)
from insouwiki.domain.documentary_sequence import (
    DocumentarySequence,
)
from insouwiki.services.simple_documentary_period_finder import (
    SimpleDocumentaryPeriodFinder,
)
from insouwiki.services.simple_documentary_theme_finder import (
    SimpleDocumentaryThemeFinder,
)


class SimpleDocumentaryNoticeBuilder:
    """Construit une notice documentaire."""

    def __init__(
        self,
        period_finder: SimpleDocumentaryPeriodFinder | None = None,
        theme_finder: SimpleDocumentaryThemeFinder | None = None,
    ):
        self.period_finder = period_finder
        self.theme_finder = theme_finder

    def build(
        self,
        document: Document,
        sequences: tuple[DocumentarySequence, ...] = (),
    ) -> DocumentaryNotice:
        documentary_contexts: tuple[str, ...] = ()
        themes: tuple[str, ...] = ()

        if (
            self.period_finder is not None
            and document.published_at is not None
        ):
            periods = self.period_finder.find_all_for(
                document.published_at.date(),
            )

            documentary_contexts = tuple(
                period.label
                for period in periods
            )

        if self.theme_finder is not None:
            documentary_themes = (
                self.theme_finder.find_for_sequences(
                    sequences,
                )
            )

            themes = tuple(
                theme.label
                for theme in documentary_themes
            )

        return DocumentaryNotice(
            documentary_contexts=documentary_contexts,
            themes=themes,
        )
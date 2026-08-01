from insouwiki.domain.documentary_clue import (
    DocumentaryClue,
)
from insouwiki.domain.documentary_search_result import (
    DocumentarySearchResult,
)


class SimpleDocumentaryClueBuilder:
    """
    Construit une piste documentaire
    à partir d'un résultat de recherche.
    """

    def build(
        self,
        result: DocumentarySearchResult,
    ) -> DocumentaryClue:
        return DocumentaryClue(
            excerpt=result.sequence_text,
            speaker=result.author,
            contexte=result.title,
            date=(
                result.published_at.date()
                if result.published_at is not None
                else None
            ),
            sequence_start=result.sequence_start,
            sequence_end=result.sequence_end,
            source_url=result.source_url,
        )

    
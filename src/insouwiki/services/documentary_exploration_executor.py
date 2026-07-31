from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.services.documentary_search_service import (
    DocumentarySearchResult,
    DocumentarySearchService,
)


class DocumentaryExplorationExecutor:
    """
    Exécute une exploration documentaire.

    Cette première version transmet le critère
    d'expression au moteur de recherche documentaire.
    """

    def __init__(
        self,
        search_service: DocumentarySearchService,
    ) -> None:
        self._search_service = search_service

    def execute(
        self,
        exploration: DocumentaryExploration,
    ) -> list[DocumentarySearchResult]:
        for criterion in exploration.criteria:
            if criterion.field == "expression":
                return self._search_service.search(
                    str(criterion.value),
                )

        return []
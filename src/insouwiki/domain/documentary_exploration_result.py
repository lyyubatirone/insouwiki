from dataclasses import dataclass

from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_inventory import (
    DocumentaryInventory,
)
from insouwiki.domain.documentary_search_result import (
    DocumentarySearchResult,
)


@dataclass(frozen=True)
class DocumentaryExplorationResult:
    """
    Résultat d'une exploration documentaire.

    Il rassemble l'exploration exécutée,
    l'inventaire documentaire retenu
    et les passages trouvés dans les sources.
    """

    exploration: DocumentaryExploration
    inventory: DocumentaryInventory
    search_results: tuple[
        DocumentarySearchResult,
        ...
    ]
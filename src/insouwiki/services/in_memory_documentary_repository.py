from insouwiki.domain.document import Document
from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_inventory import (
    DocumentaryInventory,
)
from insouwiki.domain.documentary_repository import (
    DocumentaryRepository,
)


class InMemoryDocumentaryRepository(
    DocumentaryRepository,
):
    """
    Première implémentation en mémoire
    du patrimoine documentaire.
    """

    def __init__(
        self,
        documents: tuple[Document, ...],
    ) -> None:
        self._documents = documents

    def explore(
        self,
        exploration: DocumentaryExploration,
    ) -> DocumentaryInventory:
        documents = self._documents

        for criterion in exploration.criteria:
            if criterion.field == "auteur":
                documents = tuple(
                    document
                    for document in documents
                    if document.author == criterion.value
                )

        return DocumentaryInventory(
            documents=documents,
        )
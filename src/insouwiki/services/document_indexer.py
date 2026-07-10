from abc import ABC, abstractmethod

from insouwiki.domain.document import Document


class DocumentIndexer(ABC):
    """
    Transforme un document en ressources documentaires consultables.

    L'indexation produit les ressources nécessaires
    aux recherches documentaires.
    """

    @abstractmethod
    def index(
        self,
        document: Document,
    ) -> None:
        """
        Indexe un document.
        """
        ...
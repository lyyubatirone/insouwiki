from abc import ABC, abstractmethod

from insouwiki.domain.document import Document
from insouwiki.registry.result import RegistrationResult


class DocumentRepository(ABC):

    @abstractmethod
    def register(self, document: Document) -> RegistrationResult:
        """Enregistre un document dans le registre."""
        ...

    @abstractmethod
    def exists(self, origin_key: str) -> bool:
        """Indique si un document existe déjà."""
        ...

    @abstractmethod
    def count(self) -> int:
        """Nombre de documents enregistrés."""
        ...
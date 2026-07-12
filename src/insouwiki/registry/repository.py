from abc import ABC, abstractmethod

from insouwiki.domain.document import Document
from insouwiki.registry.result import RegistrationResult
from insouwiki.domain.enums import ProcessingStatus


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

    @abstractmethod
    def find_all(self) -> list[Document]:
        """Retourne tous les documents enregistrés."""
        ...

    @abstractmethod
    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> Document | None:
        """Retourne un document à partir de son identifiant permanent."""
        ...

    @abstractmethod
    def get_by_original_url(
        self,
        original_url: str,
    ) -> Document | None:
        """Retourne un document à partir de son URL d'origine."""
        ...

    @abstractmethod
    def update_status(
        self,
        origin_key: str,
        status: ProcessingStatus,
    ) -> None:
        """
        Met à jour le statut documentaire d'un document
        identifié par sa clé d'origine.
        """
        ...
from abc import ABC, abstractmethod

from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)


class DocumentaryPeriodRepository(ABC):
    """
    Référentiel des périodes documentaires connues
    par InsouWiki.
    """

    @abstractmethod
    def list_all(
        self,
    ) -> tuple[DocumentaryPeriod, ...]:
        raise NotImplementedError

    @abstractmethod
    def register(
        self,
        period: DocumentaryPeriod,
    ) -> DocumentaryPeriod:
        raise NotImplementedError

    @abstractmethod
    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> DocumentaryPeriod | None:
        raise NotImplementedError
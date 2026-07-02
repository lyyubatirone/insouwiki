from abc import ABC, abstractmethod

from insouwiki.domain.documentary_fact import DocumentaryFact


class ContinuityFinder(ABC):
    """
    Recherche des continuités documentaires.
    """

    @abstractmethod
    def find(
        self,
        facts: list[DocumentaryFact],
    ) -> list[str]:
        """
        Retourne les observations documentaires
        de continuité détectées.
        """
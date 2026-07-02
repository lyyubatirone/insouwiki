from abc import ABC, abstractmethod

from insouwiki.domain.documentary_fact import DocumentaryFact


class DivergenceFinder(ABC):
    """
    Recherche des divergences documentaires.
    """

    @abstractmethod
    def find(
        self,
        facts: list[DocumentaryFact],
    ) -> list[str]:
        """
        Retourne les observations documentaires
        de divergence détectées.
        """
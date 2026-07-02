from abc import ABC, abstractmethod

from insouwiki.domain.documentary_fact import DocumentaryFact


class ConvergenceFinder(ABC):
    """
    Recherche des convergences documentaires.
    """

    @abstractmethod
    def find(
        self,
        facts: list[DocumentaryFact],
    ) -> list[str]:
        """
        Retourne les observations documentaires
        de convergence détectées.
        """

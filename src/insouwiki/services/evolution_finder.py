from abc import ABC, abstractmethod

from insouwiki.domain.documentary_fact import DocumentaryFact


class EvolutionFinder(ABC):
    """
    Recherche des évolutions documentaires.
    """

    @abstractmethod
    def find(
        self,
        facts: list[DocumentaryFact],
    ):
        """
        Recherche les évolutions observables à partir
        d'un ensemble de faits documentaires.
        """
        raise NotImplementedError
from abc import ABC, abstractmethod

from insouwiki.domain.corpus_status import CorpusStatus


class CorpusStatusBuilder(ABC):
    """
    Construit un état du patrimoine documentaire.

    Il observe les documents enregistrés et produit
    un instantané de l'état actuel du corpus.
    """

    @abstractmethod
    def build(self) -> CorpusStatus:
        ...
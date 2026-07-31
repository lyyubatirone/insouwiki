from abc import ABC, abstractmethod

from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_sequence import (
    DocumentarySequence,
)


class DocumentaryFactExtractor(ABC):
    @abstractmethod
    def extract(
        self,
        author: str,
        sequences: list[DocumentarySequence],
    ) -> list[DocumentaryFact]:
        raise NotImplementedError
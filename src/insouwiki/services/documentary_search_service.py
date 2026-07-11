from dataclasses import dataclass
from datetime import datetime, timedelta

from insouwiki.domain.document import Document
from insouwiki.registry.repository import DocumentRepository
from insouwiki.registry.sequence_repository import (
    DocumentarySequenceRepository,
)
from insouwiki.services.timestamp_link_builder import TimestampLinkBuilder


@dataclass
class DocumentarySearchResult:
    title: str
    author: str | None
    published_at: datetime | None
    sequence_text: str
    sequence_start: timedelta
    sequence_end: timedelta
    source_url: str
    query: str


class DocumentarySearchService:
    """
    Orchestre la recherche documentaire.

    Il recherche les séquences pertinentes, retrouve
    les documents associés et construit les liens vers les sources.
    """

    def __init__(
        self,
        document_repository: DocumentRepository,
        sequence_repository: DocumentarySequenceRepository,
        timestamp_link_builder: TimestampLinkBuilder,
    ) -> None:
        self._document_repository = document_repository
        self._sequence_repository = sequence_repository
        self._timestamp_link_builder = timestamp_link_builder

    def search(
        self,
        query: str,
    ) -> list[DocumentarySearchResult]:
        sequences = self._sequence_repository.search(query)

        results: list[DocumentarySearchResult] = []

        for sequence in sequences:
            document = self._document_repository.get_by_permanent_id(
                sequence.document_id,
            )

            if document is None:
                continue

            results.append(
                DocumentarySearchResult(
                    query=query,
                    title=document.title,
                    author=document.author,
                    published_at=document.published_at,
                    sequence_text=sequence.text,
                    sequence_start=sequence.start,
                    sequence_end=sequence.end,
                    source_url=self._timestamp_link_builder.build(
                        document=document,
                        sequence=sequence,
                    ),  
                )
            )

        return results
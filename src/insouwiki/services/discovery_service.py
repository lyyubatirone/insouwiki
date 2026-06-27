from dataclasses import dataclass

from insouwiki.collector.youtube import YouTubeCollector
from insouwiki.domain.models import DocumentSource
from insouwiki.registry.repository import DocumentRepository


@dataclass
class DiscoveryServiceResult:
    documents_discovered: int
    documents_created: int
    documents_existing: int
    documents_total_registered: int
    first_titles: list[str]


class DiscoveryService:
    def __init__(self, repository: DocumentRepository):
        self.repository = repository
        self.youtube_collector = YouTubeCollector()

    def discover(self, source: DocumentSource) -> DiscoveryServiceResult:
        report = self.youtube_collector.discover_channel(source)

        if report.errors:
            raise ValueError("\n".join(report.errors))

        created = 0
        existing = 0

        for document in report.discovered_documents:
            result = self.repository.register(document)

            if result.created:
                created += 1
            else:
                existing += 1

        first_titles = [
            document.title
            for document in report.discovered_documents[:10]
        ]

        return DiscoveryServiceResult(
            documents_discovered=len(report.discovered_documents),
            documents_created=created,
            documents_existing=existing,
            documents_total_registered=self.repository.count(),
            first_titles=first_titles,
        )
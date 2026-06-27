from dataclasses import dataclass
from time import perf_counter

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
    duration_seconds: float


class DiscoveryService:
    def __init__(self, repository: DocumentRepository):
        self.repository = repository
        self.youtube_collector = YouTubeCollector()

    def discover(self, source: DocumentSource) -> DiscoveryServiceResult:

        start = perf_counter()

        report = self.youtube_collector.discover_channel(source)

        if report.errors:
            raise ValueError("\n".join(report.errors))

        registration_results = self.repository.register_many(report.discovered_documents)

        created = sum(1 for result in registration_results if result.created)
        existing = sum(1 for result in registration_results if not result.created)

        duration = perf_counter() - start

        return DiscoveryServiceResult(
            documents_discovered=len(report.discovered_documents),
            documents_created=created,
            documents_existing=existing,
            documents_total_registered=self.repository.count(),
            first_titles=[
                document.title
                for document in report.discovered_documents[:10]
            ],
            duration_seconds=duration,
        )
import re
from dataclasses import dataclass
from time import perf_counter

from rich.diagnose import report

from insouwiki.collector.youtube import YouTubeCollector
from insouwiki.domain.discovery_request import DiscoveryRequest
from insouwiki.domain.document import Document
from insouwiki.domain.enums import ProcessingStatus
from insouwiki.domain.source import Source, SourceKind
from insouwiki.domain.source_endpoint import Platform, SourceEndpoint
from insouwiki.registry.repository import DocumentRepository
from insouwiki.registry.source_endpoint_repository import (
    SourceEndpointRepository,
)
from insouwiki.registry.source_repository import SourceRepository
from insouwiki.services.document_availability_analyzer import (
    DocumentAvailabilityAnalyzer,
)

@dataclass
class DiscoveryServiceResult:
    documents_discovered: int
    documents_created: int
    documents_existing: int
    documents_total_registered: int

    new_documents: list[Document]
    unavailable_documents: list[Document]

    first_titles: list[str]
    duration_seconds: float


class DiscoveryService:
    def __init__(
        self,
        repository: DocumentRepository,
        source_repository: SourceRepository | None = None,
        endpoint_repository: SourceEndpointRepository | None = None,
    ):
        self.repository = repository
        self.source_repository = (
            source_repository
            or SourceRepository()
        )
        self.endpoint_repository = (
            endpoint_repository
            or SourceEndpointRepository()
        )
        self.youtube_collector = YouTubeCollector()
        self._availability_analyzer = (
            DocumentAvailabilityAnalyzer()
        )

    def discover(
        self,
        request: DiscoveryRequest,
    ) -> DiscoveryServiceResult:
        start = perf_counter()

        report = self.youtube_collector.discover_channel(
            request,
        )

        if report.errors:
            raise ValueError("\n".join(report.errors))

        source_name = self._extract_source_name(report)
        registered_source = self._get_or_create_source(
            source_name
        )

        endpoint = self._get_or_create_endpoint(
            source=registered_source,
            url=str(request.url),
        )

        previous_documents = [
            document
            for document in self.repository.find_all()
            if (
                document.discovered_from_endpoint_permanent_id
                == endpoint.permanent_id
            )
        ]

        previous_origin_keys = {
            document.origin_key
            for document in previous_documents
        }

        current_origin_keys = {
            document.origin_key
            for document in report.discovered_documents
        }

        unavailable_origin_keys = (
            self._availability_analyzer
            .detect_unavailable_documents(
                previous_documents=previous_origin_keys,
                current_documents=current_origin_keys,
            )
        )

        for origin_key in unavailable_origin_keys:
            self.repository.update_status(
                origin_key=origin_key,
                status=ProcessingStatus.UNAVAILABLE,
            )

        for document in report.discovered_documents:
            document.source_permanent_id = (
                registered_source.permanent_id
            )
            document.discovered_from_endpoint_permanent_id = (
                endpoint.permanent_id
            )

        registration_results = self.repository.register_many(
            report.discovered_documents
        )

        created = sum(
            1
            for result in registration_results
            if result.created
        )
        existing = sum(
            1
            for result in registration_results
            if not result.created
        )

        duration = perf_counter() - start

        new_documents = [
            document
            for document, registration in zip(
                report.discovered_documents,
                registration_results,
            )
            if registration.created
        ]

        unavailable_documents = [
            document
            for document in previous_documents
            if document.origin_key in unavailable_origin_keys
        ]

        return DiscoveryServiceResult(
            documents_discovered=len(
                report.discovered_documents
            ),
            documents_created=created,
            documents_existing=existing,
            documents_total_registered=self.repository.count(),
            new_documents=new_documents,
            unavailable_documents=unavailable_documents,
            first_titles=[
                document.title
                for document in report.discovered_documents[:10]
            ],
            duration_seconds=duration,
        )

    def _extract_source_name(
        self,
        report,
    ) -> str:
        for document in report.discovered_documents:
            if document.author:
                return document.author

        return "Source inconnue"

    def _get_or_create_source(
        self,
        name: str,
    ) -> Source:
        existing = self.source_repository.get_by_name(
            name
        )

        if existing is not None:
            return existing

        source = Source(
            permanent_id=(
                f"source:{self._slugify(name)}"
            ),
            name=name,
            kind=SourceKind.PERSON,
        )

        return self.source_repository.create(source)

    def _get_or_create_endpoint(
        self,
        source: Source,
        url: str,
    ) -> SourceEndpoint:
        existing = self.endpoint_repository.get_by_url(
            url
        )

        if existing is not None:
            return existing

        endpoint = SourceEndpoint(
            permanent_id=(
                "endpoint:youtube:"
                f"{self._slugify(source.name)}"
            ),
            source_permanent_id=source.permanent_id,
            platform=Platform.YOUTUBE,
            url=url,
            canonical_url=url,
            external_id=self._extract_handle(url),
        )

        return self.endpoint_repository.create(endpoint)

    def _extract_handle(
        self,
        url: str,
    ) -> str | None:
        handle = url.rstrip("/").split("/")[-1]
        return handle if handle else None

    def _slugify(
        self,
        value: str,
    ) -> str:
        value = value.lower()
        value = re.sub(
            r"[^a-z0-9]+",
            "-",
            value,
        )
        value = value.strip("-")
        return value or "unknown"
from datetime import UTC, datetime

from insouwiki.domain.discovery import DiscoveryReport
from insouwiki.domain.discovery_request import DiscoveryRequest
from insouwiki.domain.document import Document
from insouwiki.domain.enums import (
    DiscoveryTargetKind,
    DocumentKind,
)
from insouwiki.domain.source import Source
from insouwiki.domain.source_endpoint import SourceEndpoint
from insouwiki.registry.result import RegistrationResult
from insouwiki.services.discovery_service import DiscoveryService


class FakeYouTubeCollector:
    def __init__(
        self,
        reports: list[DiscoveryReport],
    ) -> None:
        self._reports = reports

    def discover_channel(
        self,
        request: DiscoveryRequest,
    ) -> DiscoveryReport:
        return self._reports.pop(0)


class FakeDocumentRepository:
    def __init__(self) -> None:
        self._documents_by_origin_key: dict[str, Document] = {}

    def register_many(
        self,
        documents: list[Document],
    ) -> list[RegistrationResult]:
        results: list[RegistrationResult] = []

        for document in documents:
            existing = self._documents_by_origin_key.get(
                document.origin_key,
            )

            if existing is not None:
                document.permanent_id = existing.permanent_id

                results.append(
                    RegistrationResult(
                        document_id=existing.permanent_id,
                        created=False,
                    )
                )
                continue

            document.permanent_id = (
                f"SRC-{len(self._documents_by_origin_key) + 1:08d}"
            )

            self._documents_by_origin_key[
                document.origin_key
            ] = document

            results.append(
                RegistrationResult(
                    document_id=document.permanent_id,
                    created=True,
                )
            )

        return results

    def count(self) -> int:
        return len(self._documents_by_origin_key)


class FakeSourceRepository:
    def __init__(self) -> None:
        self._sources_by_name: dict[str, Source] = {}

    def get_by_name(
        self,
        name: str,
    ) -> Source | None:
        return self._sources_by_name.get(name)

    def create(
        self,
        source: Source,
    ) -> Source:
        self._sources_by_name[source.name] = source
        return source


class FakeSourceEndpointRepository:
    def __init__(self) -> None:
        self._endpoints_by_url: dict[str, SourceEndpoint] = {}

    def get_by_url(
        self,
        url: str,
    ) -> SourceEndpoint | None:
        return self._endpoints_by_url.get(url)

    def create(
        self,
        endpoint: SourceEndpoint,
    ) -> SourceEndpoint:
        self._endpoints_by_url[endpoint.url] = endpoint
        return endpoint


def build_document(
    video_id: str,
    title: str,
) -> Document:
    return Document(
        origin_key=f"youtube:{video_id}",
        document_kind=DocumentKind.VIDEO,
        title=title,
        original_url=(
            f"https://www.youtube.com/watch?v={video_id}"
        ),
        source_platform="youtube",
        external_id=video_id,
        author="JEAN-LUC MÉLENCHON",
        published_at=datetime(
            2026,
            7,
            1,
            tzinfo=UTC,
        ),
    )


def build_report(
    request: DiscoveryRequest,
    documents: list[Document],
) -> DiscoveryReport:
    started_at = datetime.now(UTC)

    return DiscoveryReport(
        request=request,
        discovered_documents=documents,
        started_at=started_at,
        finished_at=datetime.now(UTC),
    )


def test_second_discovery_registers_only_new_documents(
    monkeypatch,
):
    url = "https://www.youtube.com/@JLMelenchon"

    request = DiscoveryRequest(
        source_kind=DiscoveryTargetKind.YOUTUBE_CHANNEL,
        url=url,
    )

    first_report = build_report(
        request=request,
        documents=[
            build_document(
                video_id="video-1",
                title="Première vidéo",
            ),
        ],
    )

    second_report = build_report(
        request=request,
        documents=[
            build_document(
                video_id="video-1",
                title="Première vidéo",
            ),
            build_document(
                video_id="video-2",
                title="Deuxième vidéo",
            ),
        ],
    )

    collector = FakeYouTubeCollector(
        reports=[
            first_report,
            second_report,
        ]
    )

    monkeypatch.setattr(
        "insouwiki.services.discovery_service.YouTubeCollector",
        lambda: collector,
    )

    document_repository = FakeDocumentRepository()
    source_repository = FakeSourceRepository()
    endpoint_repository = FakeSourceEndpointRepository()

    service = DiscoveryService(
        repository=document_repository,
        source_repository=source_repository,
        endpoint_repository=endpoint_repository,
    )

    first_result = service.discover(request)
    second_result = service.discover(request)

    assert first_result.documents_created == 1
    assert first_result.documents_existing == 0
    assert first_result.documents_total_registered == 1

    assert second_result.documents_discovered == 2
    assert second_result.documents_created == 1
    assert second_result.documents_existing == 1
    assert second_result.documents_total_registered == 2

    assert len(source_repository._sources_by_name) == 1
    assert len(endpoint_repository._endpoints_by_url) == 1
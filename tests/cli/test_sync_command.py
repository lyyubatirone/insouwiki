from types import SimpleNamespace

from typer.testing import CliRunner

from insouwiki.cli import main as cli_main
from insouwiki.domain.document import Document
from insouwiki.domain.enums import DocumentKind


runner = CliRunner()


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
    )


class FakeDiscoveryService:
    def __init__(
        self,
        new_documents: list[Document] | None = None,
    ) -> None:
        self.received_request = None
        self._new_documents = new_documents or []

    def discover(self, request):
        self.received_request = request

        return SimpleNamespace(
            documents_discovered=5,
            documents_created=len(self._new_documents),
            documents_existing=(
                5 - len(self._new_documents)
            ),
            documents_total_registered=100,
            new_documents=self._new_documents,
            unavailable_documents=[],
            first_titles=[],
            duration_seconds=1.25,
        )


def build_fake_application(
    discovery_service: FakeDiscoveryService,
):
    return SimpleNamespace(
        discovery_service=discovery_service,
    )


def prepare_cli(
    monkeypatch,
    discovery_service: FakeDiscoveryService,
) -> None:
    fake_application = build_fake_application(
        discovery_service
    )

    monkeypatch.setattr(
        cli_main,
        "Application",
        lambda: fake_application,
    )

    monkeypatch.setattr(
        cli_main,
        "initialize_database",
        lambda: None,
    )


def test_sync_command_synchronizes_known_source(
    monkeypatch,
) -> None:
    discovery_service = FakeDiscoveryService(
        new_documents=[
            build_document(
                video_id="video-1",
                title="Première nouvelle vidéo",
            ),
            build_document(
                video_id="video-2",
                title="Deuxième nouvelle vidéo",
            ),
        ]
    )

    prepare_cli(
        monkeypatch=monkeypatch,
        discovery_service=discovery_service,
    )

    result = runner.invoke(
        cli_main.app,
        [
            "sync",
            "https://www.youtube.com/@JLMelenchon",
        ],
    )

    assert result.exit_code == 0
    assert "Synchronisation documentaire..." in result.stdout
    assert "✓ Synchronisation terminée" in result.stdout
    assert "Documents observés : 5" in result.stdout
    assert "Nouveaux documents : 2" in result.stdout
    assert "Documents déjà connus : 3" in result.stdout
    assert discovery_service.received_request is not None


def test_sync_command_displays_new_document_titles(
    monkeypatch,
) -> None:
    discovery_service = FakeDiscoveryService(
        new_documents=[
            build_document(
                video_id="video-1",
                title="Discours à Toulouse",
            ),
        ]
    )

    prepare_cli(
        monkeypatch=monkeypatch,
        discovery_service=discovery_service,
    )

    result = runner.invoke(
        cli_main.app,
        [
            "sync",
            "https://www.youtube.com/@JLMelenchon",
        ],
    )

    assert result.exit_code == 0
    assert "Nouveaux documents : 1" in result.stdout
    assert "Discours à Toulouse" in result.stdout
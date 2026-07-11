from types import SimpleNamespace

from typer.testing import CliRunner

from insouwiki.cli import main as cli_main


runner = CliRunner()


class FakeDiscoveryService:
    def __init__(self) -> None:
        self.received_request = None

    def discover(self, request):
        self.received_request = request

        return SimpleNamespace(
            documents_discovered=5,
            documents_created=2,
            documents_existing=3,
            documents_total_registered=100,
            first_titles=[],
            duration_seconds=1.25,
        )


def test_sync_command_synchronizes_known_source(
    monkeypatch,
) -> None:
    discovery_service = FakeDiscoveryService()

    fake_application = SimpleNamespace(
        discovery_service=discovery_service,
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
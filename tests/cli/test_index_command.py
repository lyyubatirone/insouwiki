from types import SimpleNamespace

from typer.testing import CliRunner

from insouwiki.cli import main as cli_main
from insouwiki.domain.document import Document
from insouwiki.domain.enums import DocumentKind


runner = CliRunner()


class FakeDocumentRepository:
    def __init__(self, document: Document) -> None:
        self._document = document
        self.requested_url: str | None = None

    def get_by_original_url(
        self,
        original_url: str,
    ) -> Document | None:
        self.requested_url = original_url

        if str(self._document.original_url) == original_url:
            return self._document

        return None


class FakeDocumentIndexer:
    def __init__(self) -> None:
        self.indexed_document: Document | None = None

    def index(
        self,
        document: Document,
    ) -> None:
        self.indexed_document = document


def test_index_command_indexes_existing_document(
    monkeypatch,
):
    url = "https://www.youtube.com/watch?v=abc123"

    document = Document(
        permanent_id="DOC-00000001",
        origin_key="youtube:video:abc123",
        document_kind=DocumentKind.VIDEO,
        title="Vidéo documentaire",
        original_url=url,
    )

    repository = FakeDocumentRepository(document)
    indexer = FakeDocumentIndexer()

    fake_application = SimpleNamespace(
        document_repository=repository,
        document_indexer=indexer,
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
            "index",
            url,
        ],
    )

    assert result.exit_code == 0
    assert repository.requested_url == url
    assert indexer.indexed_document == document
    assert "Document indexé" in result.stdout
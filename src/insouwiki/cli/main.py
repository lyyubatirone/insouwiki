import typer
from rich import print

from insouwiki.collector.youtube import YouTubeCollector
from insouwiki.domain.models import DocumentSource, SourceKind
from insouwiki.registry.postgres import PostgresDocumentRepository
from insouwiki.registry.schema import initialize_database

app = typer.Typer(
    help="Moteur documentaire d'InsouWiki",
    no_args_is_help=True,
)


@app.command()
def version():
    """Affiche la version."""
    print("[bold green]InsouWiki[/bold green]")
    print("Version : 0.1.0")


@app.command()
def discover(url: str):
    """Découvre les documents d'une source."""

    print("[bold]Découverte documentaire...[/bold]")

    initialize_database()

    source = DocumentSource(
        source_kind=SourceKind.YOUTUBE_CHANNEL,
        url=url,
    )

    collector = YouTubeCollector()
    report = collector.discover_channel(source)

    if report.errors:
        print("[red]Erreur[/red]")
        for error in report.errors:
            print(f"- {error}")
        raise typer.Exit(code=1)

    repository = PostgresDocumentRepository()

    created = 0
    existing = 0

    for document in report.discovered_documents:
        result = repository.register(document)

        if result.created:
            created += 1
        else:
            existing += 1

    print("[green]✓ Découverte terminée[/green]")
    print(f"Documents découverts : {len(report.discovered_documents)}")
    print(f"Nouveaux documents : {created}")
    print(f"Documents déjà connus : {existing}")
    print(f"Documents enregistrés : {repository.count()}")

    for document in report.discovered_documents[:10]:
        print(f"- {document.title}")


@app.command()
def scan(url: str):
    """Alias temporaire de discover."""
    discover(url)


if __name__ == "__main__":
    app()
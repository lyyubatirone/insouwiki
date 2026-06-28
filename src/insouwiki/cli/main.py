import typer
from rich import print

from insouwiki.domain.enums import DiscoveryTargetKind
from insouwiki.domain.discovery_request import DiscoveryRequest
from insouwiki.registry.postgres import PostgresDocumentRepository
from insouwiki.registry.schema import initialize_database
from insouwiki.services.discovery_service import DiscoveryService

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

    request = DiscoveryRequest(
        source_kind=DiscoveryTargetKind.YOUTUBE_CHANNEL,
        url=url,
    )

    repository = PostgresDocumentRepository()
    service = DiscoveryService(repository)

    try:
        result = service.discover(request)
    except ValueError as error:
        print("[red]Erreur[/red]")
        print(str(error))
        raise typer.Exit(code=1)

    print("[green]✓ Découverte terminée[/green]")
    print(f"Documents découverts : {result.documents_discovered}")
    print(f"Temps total : {result.duration_seconds:.2f} s")
    print(f"Nouveaux documents : {result.documents_created}")
    print(f"Documents déjà connus : {result.documents_existing}")
    print(f"Documents enregistrés : {result.documents_total_registered}")

    for title in result.first_titles:
        print(f"- {title}")


@app.command()
def scan(url: str):
    """Alias temporaire de discover."""
    discover(url)


if __name__ == "__main__":
    app()
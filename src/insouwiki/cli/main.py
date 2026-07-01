from pathlib import Path

import typer
from rich import print

from insouwiki.application import Application
from insouwiki.domain.discovery_request import DiscoveryRequest
from insouwiki.domain.document import Document
from insouwiki.domain.enums import DiscoveryTargetKind, DocumentKind
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

    request = DiscoveryRequest(
        source_kind=DiscoveryTargetKind.YOUTUBE_CHANNEL,
        url=url,
    )

    application = Application()

    try:
        result = application.discovery_service.discover(request)
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
def extract_audio(
    url: str,
    output_directory: Path = Path("tmp/audio"),
):
    """Extrait l'audio d'une vidéo YouTube."""

    print("[bold]Extraction audio...[/bold]")

    document = Document(
        permanent_id="document:manual",
        origin_key=f"manual:{url}",
        document_kind=DocumentKind.VIDEO,
        title="Document manuel",
        original_url=url,
    )

    application = Application()

    try:
        result = application.audio_extraction_service.extract(
            document=document,
            output_directory=output_directory,
        )
    except Exception as error:
        print("[red]Erreur pendant l'extraction audio[/red]")
        print(str(error))
        raise typer.Exit(code=1)

    print("[green]✓ Audio extrait[/green]")
    print(f"Document : {result.document_id}")
    print(f"Fichier  : {result.audio_path}")


@app.command()
def scan(url: str):
    """Alias temporaire de discover."""
    discover(url)


if __name__ == "__main__":
    app()
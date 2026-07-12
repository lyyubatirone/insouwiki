import re
from pathlib import Path

import typer
from rich import print
from rich.markup import escape

from insouwiki.application import Application
from insouwiki.domain.discovery_request import DiscoveryRequest
from insouwiki.domain.document import Document
from insouwiki.domain.enums import DiscoveryTargetKind, DocumentKind
from insouwiki.registry.schema import initialize_database


app = typer.Typer(
    help="Moteur documentaire d'InsouWiki",
    no_args_is_help=True,
)


def highlight_query(
    text: str,
    query: str,
) -> str:
    """
    Met en évidence la requête sans modifier le texte documentaire.

    Le texte est échappé afin que les éventuels caractères
    interprétés par Rich restent affichés tels quels.
    """
    if not query.strip():
        return escape(text)

    pattern = re.compile(
        re.escape(query),
        re.IGNORECASE,
    )

    highlighted_parts: list[str] = []
    previous_end = 0

    for match in pattern.finditer(text):
        highlighted_parts.append(
            escape(text[previous_end:match.start()])
        )
        highlighted_parts.append(
            "[bold yellow]"
            f"{escape(match.group(0))}"
            "[/bold yellow]"
        )
        previous_end = match.end()

    highlighted_parts.append(
        escape(text[previous_end:])
    )

    return "".join(highlighted_parts)


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
        print(f"- {escape(title)}")

@app.command()
def sync(url: str):
    """Synchronise une source documentaire déjà connue."""

    print("[bold]Synchronisation documentaire...[/bold]")

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

    print("[green]✓ Synchronisation terminée[/green]")
    print(f"Documents observés : {result.documents_discovered}")
    print(f"Nouveaux documents : {result.documents_created}")

    for document in result.new_documents[:10]:
        print(f"- {escape(document.title)}")

    print(f"Documents déjà connus : {result.documents_existing}")
    print(
        "Documents enregistrés : "
        f"{result.documents_total_registered}"
    )
    print(f"Temps total : {result.duration_seconds:.2f} s")


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


@app.command()
def search(query: str):
    """Recherche des séquences documentaires."""

    print(
        "[bold]Recherche documentaire :[/bold] "
        f"{escape(query)}"
    )

    initialize_database()

    application = Application()

    try:
        results = application.documentary_search_service.search(query)
    except Exception as error:
        print("[red]Erreur pendant la recherche[/red]")
        print(str(error))
        raise typer.Exit(code=1)

    result_count = len(results)

    if result_count == 0:
        print("0 séquence trouvée.")
        return

    print(f"{result_count} séquence(s) trouvée(s)")

    for result in results:
        print()
        print("[bold]────────────────────────────────────────[/bold]")

        highlighted_title = highlight_query(
            result.title,
            result.query,
        )
        print(f"[bold]{highlighted_title}[/bold]")

        if result.author:
            print(f"Auteur : {escape(result.author)}")

        if result.published_at:
            print(
                "Publié le : "
                f"{result.published_at.strftime('%d/%m/%Y')}"
            )

        start_seconds = int(
            result.sequence_start.total_seconds()
        )
        minutes, seconds = divmod(
            start_seconds,
            60,
        )

        print(f"Horodatage : {minutes:02d}:{seconds:02d}")
        print()

        highlighted_sequence = highlight_query(
            result.sequence_text,
            result.query,
        )
        print(highlighted_sequence)

        print()
        print(f"Source : {escape(result.source_url)}")


@app.command()
def index(url: str):
    """Indexe un document déjà enregistré."""

    print("[bold]Indexation documentaire...[/bold]")

    initialize_database()

    application = Application()

    document = application.document_repository.get_by_original_url(
        url,
    )

    if document is None:
        print("[red]Document inconnu.[/red]")
        print(
            "Commencez par exécuter "
            "'insouwiki discover <url-de-chaîne>'."
        )
        raise typer.Exit(code=1)

    try:
        application.document_indexer.index(document)
    except Exception as error:
        print("[red]Erreur pendant l'indexation[/red]")
        print(str(error))
        raise typer.Exit(code=1)

    print("[green]✓ Document indexé[/green]")


if __name__ == "__main__":
    app()
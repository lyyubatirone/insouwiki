import typer
from rich import print

from insouwiki.collector.youtube import YouTubeCollector

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
def scan(channel: str):
    """Analyse une chaîne YouTube."""

    handle = channel.rstrip("/").split("/")[-1]

    print("[bold]Connexion à YouTube...[/bold]")

    collector = YouTubeCollector()
    result = collector.get_channel_from_handle(handle)

    print("[green]✓ Chaîne trouvée[/green]")
    print(f"Nom : {result.title}")
    print(f"Identifiant : {result.channel_id}")
    print(f"Nombre de vidéos : {result.video_count}")
    print(f"Playlist des vidéos : {result.uploads_playlist_id}")


if __name__ == "__main__":
    app()
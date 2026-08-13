import json
from pathlib import Path

import typer
from dotenv import load_dotenv
from openai import OpenAI


AUDIO_PATH = Path(
    "tmp/experiments/EXP-0003/chunks/chunk-01.m4a"
)

OUTPUT_PATH = Path(
    "tmp/experiments/EXP-0004/whisper-chunk-01.json"
)


def main(
    execute: bool = typer.Option(
        False,
        "--execute",
        help=(
            "Autorise explicitement "
            "l'appel payant à l'API."
        ),
    ),
) -> None:
    typer.echo(
        "EXP-0004 — Référence temporelle Whisper"
    )
    typer.echo(
        "Modèle : whisper-1"
    )
    typer.echo(
        f"Audio : {AUDIO_PATH}"
    )
    typer.echo()

    if not AUDIO_PATH.exists():
        typer.echo(
            "Le chunk audio est introuvable."
        )
        raise typer.Exit(code=1)

    if not execute:
        typer.echo(
            "Mode simulation : "
            "aucun appel API effectué."
        )
        typer.echo(
            "Utiliser --execute pour autoriser "
            "explicitement l'appel payant."
        )
        return

    confirmed = typer.confirm(
        "Cet appel utilise l'API OpenAI "
        "et peut être payant. Continuer ?",
        default=False,
    )

    if not confirmed:
        typer.echo(
            "Expérience annulée."
        )
        return

    load_dotenv()

    client = OpenAI()

    with AUDIO_PATH.open(
        "rb"
    ) as audio_file:
        response = (
            client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="fr",
                response_format="verbose_json",
                timestamp_granularities=[
                    "segment",
                ],
            )
        )

    response_data = response.model_dump(
        mode="json",
    )

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_PATH.open(
        "w",
        encoding="utf-8",
    ) as output_file:
        json.dump(
            response_data,
            output_file,
            ensure_ascii=False,
            indent=2,
        )

    segments = response_data.get(
        "segments",
        [],
    )

    typer.echo()
    typer.echo(
        "✓ Référence Whisper créée"
    )
    typer.echo(
        f"Résultat : {OUTPUT_PATH}"
    )
    typer.echo(
        f"Segments : {len(segments)}"
    )
    typer.echo(
        f"Usage : {response_data.get('usage')}"
    )


if __name__ == "__main__":
    typer.run(main)
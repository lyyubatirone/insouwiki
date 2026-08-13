import json
from pathlib import Path

import typer
from dotenv import load_dotenv
from openai import OpenAI


AUDIO_PATH = Path(
    "tmp/experiments/EXP-0005/case-a-acoustic.m4a"
)

OUTPUT_DIRECTORY = Path(
    "tmp/experiments/EXP-0005"
)

SUPPORTED_MODELS = {
    "gpt-4o-mini-transcribe",
    "whisper-1",
}


def transcribe_mini(
    client: OpenAI,
):
    with AUDIO_PATH.open("rb") as audio_file:
        return client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio_file,
            language="fr",
            response_format="json",
        )


def transcribe_whisper(
    client: OpenAI,
):
    with AUDIO_PATH.open("rb") as audio_file:
        return client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="fr",
            response_format="verbose_json",
            timestamp_granularities=[
                "segment",
            ],
        )


def main(
    model: str = typer.Argument(...),
    execute: bool = typer.Option(
        False,
        "--execute",
        help=(
            "Autorise explicitement "
            "l'appel payant à l'API."
        ),
    ),
) -> None:
    if model not in SUPPORTED_MODELS:
        typer.echo(
            f"Modèle non autorisé : {model}"
        )
        raise typer.Exit(code=1)

    if not AUDIO_PATH.exists():
        typer.echo(
            f"Audio introuvable : {AUDIO_PATH}"
        )
        raise typer.Exit(code=1)

    typer.echo(
        "EXP-0005-A — Résistance acoustique"
    )
    typer.echo(
        f"Modèle : {model}"
    )
    typer.echo(
        f"Audio : {AUDIO_PATH}"
    )
    typer.echo()

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

    OUTPUT_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    if model == "gpt-4o-mini-transcribe":
        response = transcribe_mini(
            client,
        )
    elif model == "whisper-1":
        response = transcribe_whisper(
            client,
        )
    else:
        raise typer.Exit(code=1)

    response_data = response.model_dump(
        mode="json",
    )

    output_path = (
        OUTPUT_DIRECTORY
        / f"case-a-{model}.json"
    )

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as output_file:
        json.dump(
            response_data,
            output_file,
            ensure_ascii=False,
            indent=2,
        )

    typer.echo()
    typer.echo(
        "✓ Transcription terminée"
    )
    typer.echo(
        f"Résultat : {output_path}"
    )

    segments = response_data.get(
        "segments",
        [],
    )

    typer.echo(
        f"Segments : {len(segments)}"
    )

    usage = response_data.get(
        "usage"
    )

    if usage:
        typer.echo(
            f"Usage : {usage}"
        )


if __name__ == "__main__":
    typer.run(main)
    
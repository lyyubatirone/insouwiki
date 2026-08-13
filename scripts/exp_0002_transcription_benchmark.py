import json
from pathlib import Path

import typer
from dotenv import load_dotenv
from openai import OpenAI


AUDIO_PATH = Path(
    "tmp/audio/GXLhDojRHfo.m4a"
)

OUTPUT_DIRECTORY = Path(
    "tmp/experiments/EXP-0002"
)

SUPPORTED_MODELS = {
    "whisper-1",
    "gpt-4o-mini-transcribe",
    "gpt-4o-transcribe",
    "gpt-4o-transcribe-diarize",
}


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

def transcribe_gpt4o_mini(
    client: OpenAI,
):
    with AUDIO_PATH.open("rb") as audio_file:
        return client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio_file,
            language="fr",
            response_format="json",
        )

def transcribe_gpt4o(
    client: OpenAI,
):
    with AUDIO_PATH.open("rb") as audio_file:
        return client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file,
            language="fr",
            response_format="json",
        )


def transcribe_diarized(
    client: OpenAI,
):
    with AUDIO_PATH.open("rb") as audio_file:
        return client.audio.transcriptions.create(
            model="gpt-4o-transcribe-diarize",
            file=audio_file,
            language="fr",
            response_format="diarized_json",
            chunking_strategy="auto",
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
):
    if model not in SUPPORTED_MODELS:
        typer.echo(
            "Modèle non autorisé "
            f"pour EXP-0002 : {model}"
        )
        raise typer.Exit(code=1)

    if not AUDIO_PATH.exists():
        typer.echo(
            "Fichier audio introuvable : "
            f"{AUDIO_PATH}"
        )
        raise typer.Exit(code=1)

    typer.echo(
        "EXP-0002 — Benchmark transcription"
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

    if model == "whisper-1":
        response = transcribe_whisper(
            client,
        )
    elif model == "gpt-4o-mini-transcribe":
        response = transcribe_gpt4o_mini(
            client,
        )
    elif model == "gpt-4o-transcribe":
        response = transcribe_gpt4o(
            client,
        )
    elif model == "gpt-4o-transcribe-diarize":
        response = transcribe_diarized(
            client,
        )
    else:
        raise typer.Exit(code=1)

    response_data = response.model_dump(
        mode="json",
    )

    output_path = (
        OUTPUT_DIRECTORY
        / f"{model}.json"
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

    if (
        model
        == "gpt-4o-transcribe-diarize"
    ):
        speakers = {
            segment.get("speaker")
            for segment in segments
            if segment.get("speaker")
        }

        typer.echo(
            "Locuteurs détectés : "
            f"{len(speakers)}"
        )


if __name__ == "__main__":
    typer.run(main)
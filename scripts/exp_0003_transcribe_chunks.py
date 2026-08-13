import json
from pathlib import Path

import typer
from dotenv import load_dotenv
from openai import OpenAI


CHUNKS_DIRECTORY = Path(
    "tmp/experiments/EXP-0003/chunks"
)

OUTPUT_DIRECTORY = Path(
    "tmp/experiments/EXP-0003/transcriptions"
)

CHUNK_OFFSETS = {
    "chunk-01": 0,
    "chunk-02": 175,
    "chunk-03": 350,
    "chunk-04": 525,
    "chunk-05": 700,
}


def main(
    execute: bool = typer.Option(
        False,
        "--execute",
        help=(
            "Autorise explicitement "
            "les appels payants à l'API."
        ),
    ),
) -> None:
    chunk_paths = sorted(
        CHUNKS_DIRECTORY.glob("chunk-*.m4a")
    )

    if not chunk_paths:
        typer.echo(
            "Aucun chunk audio trouvé."
        )
        raise typer.Exit(code=1)

    typer.echo(
        "EXP-0003 — Transcription par chunks"
    )
    typer.echo(
        "Modèle : gpt-4o-mini-transcribe"
    )
    typer.echo(
        f"Chunks : {len(chunk_paths)}"
    )
    typer.echo()

    for chunk_path in chunk_paths:
        offset = CHUNK_OFFSETS.get(
            chunk_path.stem
        )

        typer.echo(
            f"{chunk_path.name} "
            f"| offset absolu : {offset}s"
        )

    typer.echo()

    if not execute:
        typer.echo(
            "Mode simulation : "
            "aucun appel API effectué."
        )
        typer.echo(
            "Utiliser --execute pour autoriser "
            "explicitement les appels payants."
        )
        return

    confirmed = typer.confirm(
        "Les 5 chunks vont être transcrits "
        "via l'API OpenAI. Continuer ?",
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

    for index, chunk_path in enumerate(
        chunk_paths,
        start=1,
    ):
        typer.echo()
        typer.echo(
            f"Transcription "
            f"{index}/{len(chunk_paths)} "
            f": {chunk_path.name}"
        )

        with chunk_path.open(
            "rb"
        ) as audio_file:
            response = (
                client.audio.transcriptions.create(
                    model=(
                        "gpt-4o-mini-transcribe"
                    ),
                    file=audio_file,
                    language="fr",
                    response_format="json",
                )
            )

        response_data = response.model_dump(
            mode="json",
        )

        output_data = {
            "chunk": chunk_path.name,
            "offset_seconds": (
                CHUNK_OFFSETS[
                    chunk_path.stem
                ]
            ),
            "transcription": response_data,
        }

        output_path = (
            OUTPUT_DIRECTORY
            / f"{chunk_path.stem}.json"
        )

        with output_path.open(
            "w",
            encoding="utf-8",
        ) as output_file:
            json.dump(
                output_data,
                output_file,
                ensure_ascii=False,
                indent=2,
            )

        usage = response_data.get(
            "usage"
        )

        typer.echo(
            f"✓ {output_path}"
        )

        if usage:
            typer.echo(
                f"  Usage : {usage}"
            )

    typer.echo()
    typer.echo(
        "✓ EXP-0003 : "
        "5 chunks transcrits."
    )


if __name__ == "__main__":
    typer.run(main)
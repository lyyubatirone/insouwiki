from pathlib import Path
import subprocess


AUDIO_PATH = Path(
    "tmp/audio/WyjX4W0STmM.m4a"
)

OUTPUT_DIRECTORY = Path(
    "tmp/experiments/EXP-0003/chunks"
)

CHUNK_SECONDS = 180
OVERLAP_SECONDS = 5


def main() -> None:
    if not AUDIO_PATH.exists():
        raise FileNotFoundError(
            f"Audio introuvable : {AUDIO_PATH}"
        )

    OUTPUT_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    duration_seconds = 13 * 60 + 52

    start = 0
    index = 1

    while start < duration_seconds:
        end = min(
            start + CHUNK_SECONDS,
            duration_seconds,
        )

        chunk_duration = end - start

        output_path = (
            OUTPUT_DIRECTORY
            / f"chunk-{index:02d}.m4a"
        )

        command = [
            "ffmpeg",
            "-y",
            "-ss",
            str(start),
            "-i",
            str(AUDIO_PATH),
            "-t",
            str(chunk_duration),
            "-vn",
            "-c:a",
            "copy",
            str(output_path),
        ]

        subprocess.run(
            command,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        print(
            f"{output_path} | "
            f"{start:>4}s -> {end:>4}s"
        )

        if end >= duration_seconds:
            break

        start = (
            end - OVERLAP_SECONDS
        )

        index += 1


if __name__ == "__main__":
    main()
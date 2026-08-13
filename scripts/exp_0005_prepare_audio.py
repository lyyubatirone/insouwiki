import subprocess
from pathlib import Path


SOURCE_PATH = Path(
    "tmp/audio/73dR5vv9hIk.m4a"
)

OUTPUT_PATH = Path(
    "tmp/experiments/EXP-0005/"
    "case-a-acoustic.m4a"
)


def main() -> None:
    SOURCE_PATH = Path(
        "tmp/audio/xEUD8F_HP1Y.m4a"
    )

    OUTPUT_PATH = Path(
        "tmp/experiments/EXP-0005/"
        "case-b-diction.m4a"
    )

    command = [
        "ffmpeg",
        "-y",
        "-ss",
        "220",
        "-i",
        str(SOURCE_PATH),
        "-t",
        "180",
        "-vn",
        "-c:a",
        "copy",
        str(OUTPUT_PATH),
    ]

    subprocess.run(
        command,
        check=True,
    )

    print("EXP-0005-B — Échantillon diction")
    print()
    print(f"Source : {SOURCE_PATH}")
    print("Passage : 03:40 -> 06:40")
    print(f"Résultat : {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
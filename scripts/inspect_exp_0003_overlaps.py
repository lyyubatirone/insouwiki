import json
from pathlib import Path


TRANSCRIPTIONS_DIRECTORY = Path(
    "tmp/experiments/EXP-0003/transcriptions"
)


def load_text(
    chunk_number: int,
) -> str:
    path = (
        TRANSCRIPTIONS_DIRECTORY
        / f"chunk-{chunk_number:02d}.json"
    )

    data = json.loads(
        path.read_text(
            encoding="utf-8",
        )
    )

    return (
        data["transcription"]
        .get("text", "")
        .strip()
    )


for chunk_number in range(1, 5):
    current_text = load_text(
        chunk_number,
    )

    next_text = load_text(
        chunk_number + 1,
    )

    print()
    print(
        "=" * 70
    )
    print(
        f"FRONTIÈRE "
        f"{chunk_number} → "
        f"{chunk_number + 1}"
    )
    print(
        "=" * 70
    )

    print()
    print(
        f"FIN chunk-{chunk_number:02d} :"
    )
    print()
    print(
        current_text[-700:]
    )

    print()
    print(
        f"DÉBUT chunk-{chunk_number + 1:02d} :"
    )
    print()
    print(
        next_text[:700]
    )
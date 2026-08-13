import json
import re
from difflib import SequenceMatcher
from pathlib import Path


TRANSCRIPTIONS_DIRECTORY = Path(
    "tmp/experiments/EXP-0003/transcriptions"
)


def load_text(chunk_number: int) -> str:
    path = (
        TRANSCRIPTIONS_DIRECTORY
        / f"chunk-{chunk_number:02d}.json"
    )

    data = json.loads(
        path.read_text(encoding="utf-8")
    )

    return (
        data["transcription"]
        .get("text", "")
        .strip()
    )


def normalize(text: str) -> list[str]:
    return re.findall(
        r"\w+",
        text.casefold(),
        flags=re.UNICODE,
    )


def find_overlap(
    left_text: str,
    right_text: str,
) -> None:
    left_words = normalize(left_text)
    right_words = normalize(right_text)

    # Nous ne comparons que la zone susceptible
    # de correspondre aux 5 secondes communes.
    left_tail = left_words[-80:]
    right_head = right_words[:80]

    matcher = SequenceMatcher(
        None,
        left_tail,
        right_head,
        autojunk=False,
    )

    match = matcher.find_longest_match(
        0,
        len(left_tail),
        0,
        len(right_head),
    )

    matched_words = left_tail[
        match.a : match.a + match.size
    ]

    print(
        f"Correspondance : {match.size} mots"
    )

    print(
        "Texte commun :",
        " ".join(matched_words),
    )


def main() -> None:
    for chunk_number in range(1, 5):
        print()
        print("=" * 70)
        print(
            f"FRONTIÈRE "
            f"{chunk_number} → "
            f"{chunk_number + 1}"
        )
        print("=" * 70)

        find_overlap(
            load_text(chunk_number),
            load_text(chunk_number + 1),
        )


if __name__ == "__main__":
    main()
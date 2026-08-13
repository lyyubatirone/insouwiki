import json
import re
from difflib import SequenceMatcher
from pathlib import Path


WHISPER_PATH = Path(
    "tmp/experiments/EXP-0004/"
    "whisper-chunk-01.json"
)

MINI_PATH = Path(
    "tmp/experiments/EXP-0003/"
    "transcriptions/chunk-01.json"
)


def normalize_words(
    text: str,
) -> list[str]:
    return re.findall(
        r"\w+",
        text.casefold(),
        flags=re.UNICODE,
    )


whisper_data = json.loads(
    WHISPER_PATH.read_text(
        encoding="utf-8",
    )
)

mini_data = json.loads(
    MINI_PATH.read_text(
        encoding="utf-8",
    )
)

whisper_segments = whisper_data.get(
    "segments",
    [],
)

mini_text = (
    mini_data["transcription"]
    .get("text", "")
    .strip()
)

mini_words = normalize_words(
    mini_text
)

whisper_words: list[str] = []

segment_word_ranges: list[
    tuple[int, int]
] = []

for segment in whisper_segments:
    segment_words = normalize_words(
        segment.get("text", "")
    )

    start_index = len(
        whisper_words
    )

    whisper_words.extend(
        segment_words
    )

    end_index = len(
        whisper_words
    )

    segment_word_ranges.append(
        (
            start_index,
            end_index,
        )
    )


matcher = SequenceMatcher(
    None,
    whisper_words,
    mini_words,
    autojunk=False,
)

opcodes = matcher.get_opcodes()


whisper_to_mini: dict[
    int,
    int,
] = {}

for tag, i1, i2, j1, j2 in opcodes:
    if tag == "equal":
        for offset in range(
            i2 - i1
        ):
            whisper_to_mini[
                i1 + offset
            ] = (
                j1 + offset
            )


print(
    "EXP-0004 — "
    "Alignement segment par segment"
)
print()

for segment, word_range in zip(
    whisper_segments,
    segment_word_ranges,
):
    whisper_start, whisper_end = (
        word_range
    )

    matched_mini_indexes = [
        whisper_to_mini[index]
        for index in range(
            whisper_start,
            whisper_end,
        )
        if index in whisper_to_mini
    ]

    whisper_segment_words = (
        whisper_end
        - whisper_start
    )

    matched_count = len(
        matched_mini_indexes
    )

    if whisper_segment_words:
        confidence = (
            matched_count
            / whisper_segment_words
        )
    else:
        confidence = 0.0

    if matched_mini_indexes:
        mini_start = min(
            matched_mini_indexes
        )

        mini_end = max(
            matched_mini_indexes
        ) + 1

        mini_segment_words = (
            mini_words[
                mini_start:mini_end
            ]
        )

        mini_segment_text = " ".join(
            mini_segment_words
        )
    else:
        mini_segment_text = (
            "[aucun alignement]"
        )

    start = segment.get(
        "start",
        0,
    )

    end = segment.get(
        "end",
        0,
    )

    whisper_text = (
        segment.get(
            "text",
            "",
        )
        .strip()
    )

    print(
        "=" * 70
    )

    print(
        f"{start:7.2f} -> "
        f"{end:7.2f}"
    )

    print(
        f"Confiance : "
        f"{confidence:.2%}"
    )

    print()

    print(
        "WHISPER :"
    )

    print(
        whisper_text
    )

    print()

    print(
        "MINI ALIGNÉ :"
    )

    print(
        mini_segment_text
    )

    print()
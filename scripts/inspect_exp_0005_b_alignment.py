import json
import re
from difflib import SequenceMatcher
from pathlib import Path


WHISPER_PATH = Path(
    "tmp/experiments/EXP-0005/"
    "case-b-whisper-1.json"
)

MINI_PATH = Path(
    "tmp/experiments/EXP-0005/"
    "case-b-gpt-4o-mini-transcribe.json"
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

whisper_text = " ".join(
    segment.get("text", "").strip()
    for segment in whisper_segments
)

mini_text = (
    mini_data.get("text", "")
    .strip()
)

whisper_words = normalize_words(
    whisper_text
)

mini_words = normalize_words(
    mini_text
)

matcher = SequenceMatcher(
    None,
    whisper_words,
    mini_words,
    autojunk=False,
)

matching_blocks = [
    block
    for block in matcher.get_matching_blocks()
    if block.size > 0
]

matched_words = sum(
    block.size
    for block in matching_blocks
)

print(
    "EXP-0005-B — Alignement mini / Whisper"
)
print()

print(
    f"Segments Whisper : "
    f"{len(whisper_segments)}"
)

print(
    f"Mots Whisper : "
    f"{len(whisper_words)}"
)

print(
    f"Mots mini : "
    f"{len(mini_words)}"
)

print(
    f"Mots communs alignés : "
    f"{matched_words}"
)

print(
    f"Similarité globale : "
    f"{matcher.ratio():.3f}"
)

print()
print("Principales correspondances :")
print()

largest_blocks = sorted(
    matching_blocks,
    key=lambda block: block.size,
    reverse=True,
)[:10]

for block in largest_blocks:
    words = mini_words[
        block.b : block.b + block.size
    ]

    print(
        f"{block.size:3d} mots | "
        + " ".join(words[:20])
    )
import json
from pathlib import Path


path = Path(
    "tmp/experiments/EXP-0002/whisper-1.json"
)

data = json.loads(
    path.read_text(encoding="utf-8")
)

segments = data.get("segments", [])


def print_segments_around(
    target_seconds: float,
    window_seconds: float = 12.0,
) -> None:
    start_window = (
        target_seconds - window_seconds
    )

    end_window = (
        target_seconds + window_seconds
    )

    print()
    print(
        "========================================"
    )
    print(
        f"Autour de {target_seconds:.0f} s"
    )
    print(
        "========================================"
    )

    for segment in segments:
        start = segment.get("start", 0)
        end = segment.get("end", 0)

        if (
            end >= start_window
            and start <= end_window
        ):
            text = (
                segment.get("text", "")
                .strip()
            )

            print(
                f"{start:7.2f} -> "
                f"{end:7.2f} | "
                f"{text}"
            )


print(f"Langue : {data.get('language')}")
print(f"Durée : {data.get('duration')} s")
print(f"Segments : {len(segments)}")

reference_times = [
    30,
    120,
    300,
    480,
    660,
]

for reference_time in reference_times:
    print_segments_around(
        reference_time,
    )
import json
from collections import Counter, defaultdict
from pathlib import Path


path = Path(
    "tmp/experiments/EXP-0002/"
    "gpt-4o-transcribe-diarize.json"
)

data = json.loads(
    path.read_text(encoding="utf-8")
)

segments = data.get("segments", [])

print("Champs racine :")
print(sorted(data.keys()))
print()

print(f"Segments : {len(segments)}")

segment_counts = Counter()

speaker_durations = defaultdict(float)

for segment in segments:
    speaker = segment.get("speaker")

    if not speaker:
        continue

    segment_counts[speaker] += 1

    start = float(
        segment.get("start", 0)
    )

    end = float(
        segment.get("end", 0)
    )

    speaker_durations[speaker] += max(
        0,
        end - start,
    )

print(
    f"Locuteurs : {len(segment_counts)}"
)
print()

print("Temps de parole par locuteur :")
print()

total_speech = sum(
    speaker_durations.values()
)

for speaker, duration in sorted(
    speaker_durations.items(),
    key=lambda item: item[1],
    reverse=True,
):
    minutes = int(
        duration // 60
    )

    seconds = duration % 60

    percentage = (
        100 * duration / total_speech
        if total_speech
        else 0
    )

    print(
        f"  {speaker}: "
        f"{minutes:02d} min "
        f"{seconds:05.2f} s "
        f"| {percentage:5.1f} % "
        f"| {segment_counts[speaker]} segments"
    )

print()
print("Locuteurs significatifs (> 30 s) :")
print()

significant_speakers = [
    speaker
    for speaker, duration
    in speaker_durations.items()
    if duration >= 30
]

for speaker in sorted(
    significant_speakers,
    key=lambda speaker: (
        speaker_durations[speaker]
    ),
    reverse=True,
):
    print(
        f"  {speaker}"
    )

print()
print(
    "Nombre de locuteurs significatifs : "
    f"{len(significant_speakers)}"
)
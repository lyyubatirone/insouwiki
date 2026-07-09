"""
Leçons documentaires du DocumentaryReasoningAnalyzer.

Chaque test représente une connaissance documentaire
que l'Analyseur doit conserver tout au long de son évolution.
"""

from datetime import timedelta

from insouwiki.domain.transcription_segment import TranscriptionSegment
from insouwiki.services.documentary_reasoning_analyzer import (
    DocumentaryReasoningAnalyzer,
)


def test_detects_explicit_topic_change():
    analyzer = DocumentaryReasoningAnalyzer()

    current_segment = TranscriptionSegment(
        start=timedelta(seconds=0),
        end=timedelta(seconds=5),
        speaker="Jean Dupont",
        text="La retraite à 60 ans est une nécessité.",
    )

    next_segment = TranscriptionSegment(
        start=timedelta(seconds=5),
        end=timedelta(seconds=10),
        speaker="Jean Dupont",
        text="Passons maintenant à la planification écologique.",
    )

    assert (
        analyzer.belongs_to_same_reasoning(
            current_segment,
            next_segment,
        )
        is False
    )

def test_speaker_change_does_not_break_reasoning():
    analyzer = DocumentaryReasoningAnalyzer()

    current_segment = TranscriptionSegment(
        start=timedelta(seconds=0),
        end=timedelta(seconds=3),
        speaker="Journaliste",
        text="Pourquoi proposez-vous la retraite à 60 ans ?",
    )

    next_segment = TranscriptionSegment(
        start=timedelta(seconds=3),
        end=timedelta(seconds=12),
        speaker="Jean Dupont",
        text="Parce qu'elle permet à chacun de profiter de sa retraite.",
    )

    assert (
        analyzer.belongs_to_same_reasoning(
            current_segment,
            next_segment,
        )
        is True
    )

def test_question_and_answer_belong_to_same_reasoning():
    analyzer = DocumentaryReasoningAnalyzer()

    current_segment = TranscriptionSegment(
        start=timedelta(seconds=0),
        end=timedelta(seconds=4),
        speaker="Journaliste",
        text="Pourquoi proposez-vous la retraite à 60 ans ?",
    )

    next_segment = TranscriptionSegment(
        start=timedelta(seconds=4),
        end=timedelta(seconds=12),
        speaker="Jean Dupont",
        text="Parce qu'elle permet à chacun de vivre dignement après sa vie de travail.",
    )

    assert (
        analyzer.belongs_to_same_reasoning(
            current_segment,
            next_segment,
        )
        is True
    )

def test_analyzes_reasoning_continuity_with_documentary_analysis():
    analyzer = DocumentaryReasoningAnalyzer()

    current_segment = TranscriptionSegment(
        start=timedelta(seconds=0),
        end=timedelta(seconds=4),
        speaker="Journaliste",
        text="Pourquoi proposez-vous la retraite à 60 ans ?",
    )

    next_segment = TranscriptionSegment(
        start=timedelta(seconds=4),
        end=timedelta(seconds=12),
        speaker="Jean Dupont",
        text="Parce qu'elle permet à chacun de vivre dignement après sa vie de travail.",
    )

    analysis = analyzer.analyze_reasoning_continuity(
        current_segment,
        next_segment,
    )

    assert analysis.observations == [
        "Point d'interrogation",
        "Changement de locuteur",
    ]

    assert analysis.indicators == [
        "Continuité dialogique",
    ]

    assert analysis.explanation == (
        "La réponse répond directement à la question."
    )

    assert analysis.proposed_conclusion == (
        "Continuité documentaire."
    )
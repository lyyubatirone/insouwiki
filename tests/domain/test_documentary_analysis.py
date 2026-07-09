from insouwiki.domain.documentary_analysis import (
    DocumentaryAnalysis,
)


def test_documentary_analysis_contains_reasoning():
    analysis = DocumentaryAnalysis(
        observations=[
            "Point d'interrogation",
            "Changement de locuteur",
        ],
        indicators=[
            "Continuité dialogique",
        ],
        explanation=(
            "La réponse répond directement à la question."
        ),
        proposed_conclusion=(
            "Continuité documentaire."
        ),
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
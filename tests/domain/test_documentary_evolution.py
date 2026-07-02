from insouwiki.domain.documentary_evolution import (
    DocumentaryEvolution,
)


def test_create_documentary_evolution():
    evolution = DocumentaryEvolution(
        permanent_id="EVOL-00000001",
        supporting_fact_ids=[
            "FACT-00000001",
            "FACT-00000002",
        ],
        summary="Évolution documentaire.",
    )

    assert evolution.permanent_id == "EVOL-00000001"

    assert evolution.supporting_fact_ids == [
        "FACT-00000001",
        "FACT-00000002",
    ]

    assert evolution.summary == "Évolution documentaire."
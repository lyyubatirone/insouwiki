import pytest

from insouwiki.domain.knowledge import Knowledge


def test_knowledge_creation():
    knowledge = Knowledge(
        permanent_id="KNOW-00000001",
        title="Autonomie de la Corse",
        summary="Plusieurs faits documentaires décrivent une position favorable à l'autonomie de la Corse.",
        supporting_fact_ids=["FACT-00000001", "FACT-00000002"],
    )

    assert knowledge.permanent_id == "KNOW-00000001"
    assert knowledge.title == "Autonomie de la Corse"
    assert (
        knowledge.summary
        == "Plusieurs faits documentaires décrivent une position favorable à l'autonomie de la Corse."
    )
    assert knowledge.supporting_fact_ids == [
        "FACT-00000001",
        "FACT-00000002",
    ]


def test_knowledge_requires_at_least_one_supporting_fact():
    with pytest.raises(ValueError):
        Knowledge(
            permanent_id="KNOW-00000001",
            title="Connaissance invalide",
            summary="Cette connaissance ne référence aucun fait documentaire.",
            supporting_fact_ids=[],
        )
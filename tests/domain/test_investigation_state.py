from insouwiki.domain.investigation.investigation_state import (
    InvestigationState,
)


def test_investigation_state_contains_question():
    state = InvestigationState(
        question="retraite à 60 ans",
    )

    assert state.question == "retraite à 60 ans"

def test_can_add_personality_to_investigation():
    state = InvestigationState(
        question="Corse",
    )

    new_state = state.with_personality(
        "Jean-Luc Mélenchon",
    )

    assert new_state.question == "Corse"

    assert new_state.personalities == (
        "Jean-Luc Mélenchon",
    )

def test_can_remove_personality():
    state = (
        InvestigationState(
            question="Corse",
        )
        .with_personality(
            "Jean-Luc Mélenchon",
        )
    )

    new_state = state.without_personality(
        "Jean-Luc Mélenchon",
    )

    assert new_state.personalities == ()

def test_can_add_second_personality():
    state = (
        InvestigationState(
            question="Corse",
        )
        .with_personality(
            "Jean-Luc Mélenchon",
        )
        .with_personality(
            "Manuel Bompard",
        )
    )

    assert state.personalities == (
        "Jean-Luc Mélenchon",
        "Manuel Bompard",
    )

def test_cannot_add_same_personality_twice():
    state = (
        InvestigationState(
            question="Corse",
        )
        .with_personality(
            "Jean-Luc Mélenchon",
        )
        .with_personality(
            "Jean-Luc Mélenchon",
        )
    )

    assert state.personalities == (
        "Jean-Luc Mélenchon",
    )

def test_can_select_context():
    state = InvestigationState(
        question="Corse",
    )

    new_state = state.with_context(
        "Campagne présidentielle 2022",
    )

    assert new_state.context == (
        "Campagne présidentielle 2022"
    )

def test_can_change_context():
    state = (
        InvestigationState(
            question="Corse",
        )
        .with_context(
            "Campagne présidentielle 2022",
        )
    )

    new_state = state.with_context(
        "XVIIe législature",
    )

    assert new_state.context == (
        "XVIIe législature"
    )

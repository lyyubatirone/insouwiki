from insouwiki.domain.exploration_intent import ExplorationIntent


def test_exploration_intents_are_stable():
    assert ExplorationIntent.UNDERSTAND.value == "understand"
    assert ExplorationIntent.COMPARE.value == "compare"
    assert ExplorationIntent.VERIFY.value == "verify"
    assert ExplorationIntent.CONTEXT.value == "context"
    assert ExplorationIntent.FOLLOW_EVOLUTION.value == "follow_evolution"
    assert ExplorationIntent.DISCOVER.value == "discover"
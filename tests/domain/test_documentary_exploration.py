from insouwiki.domain.documentary_exploration import DocumentaryExploration
from insouwiki.domain.exploration_intent import ExplorationIntent


def test_create_documentary_exploration():
    exploration = DocumentaryExploration(
        intent=ExplorationIntent.UNDERSTAND,
        subjects=[
            "Retraites",
        ],
        observations=[
            "Cette affirmation apparaît de manière récurrente dans les sources documentaires disponibles.",
        ],
    )

    assert exploration.intent == ExplorationIntent.UNDERSTAND

    assert exploration.subjects == [
        "Retraites",
    ]

    assert exploration.observations == [
        "Cette affirmation apparaît de manière récurrente dans les sources documentaires disponibles.",
    ]
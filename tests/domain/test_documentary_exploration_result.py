from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_exploration_result import (
    DocumentaryExplorationResult,
)
from insouwiki.domain.documentary_inventory import (
    DocumentaryInventory,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)


def test_exploration_result_contains_exploration():
    question = DocumentaryQuestion(
        text="Que disent les sources sur les retraites ?",
    )

    exploration = DocumentaryExploration(
        intent=ExplorationIntent.UNDERSTAND,
        question=question,
        criteria=(),
        subjects=[],
        observations=[],
    )

    inventory = DocumentaryInventory()

    result = DocumentaryExplorationResult(
        exploration=exploration,
        inventory=inventory,
        search_results=(),
    )

    assert result.exploration is exploration
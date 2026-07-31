from unittest.mock import Mock

from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from insouwiki.domain.documentary_exploration import (
    DocumentaryExploration,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)
from insouwiki.services.documentary_exploration_executor import (
    DocumentaryExplorationExecutor,
)


def test_searches_using_expression_criterion():
    search_service = Mock()
    search_service.search.return_value = []

    executor = DocumentaryExplorationExecutor(
        search_service=search_service,
    )

    exploration = DocumentaryExploration(
        intent=ExplorationIntent.UNDERSTAND,
        question=DocumentaryQuestion(
            text="Retraite à 60 ans",
        ),
        criteria=(
            DocumentaryCriterion(
                field="expression",
                value="60 ans",
            ),
        ),
        subjects=["Retraites"],
        observations=[],
    )

    result = executor.execute(
        exploration,
    )

    search_service.search.assert_called_once_with(
        "60 ans",
    )
    assert result == []
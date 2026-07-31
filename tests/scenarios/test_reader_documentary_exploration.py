from unittest.mock import Mock

from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.documentary_subject import (
    DocumentarySubject,
)
from insouwiki.domain.exploration_intent import (
    ExplorationIntent,
)
from insouwiki.services.documentary_exploration_executor import (
    DocumentaryExplorationExecutor,
)
from insouwiki.services.simple_continuity_finder import (
    SimpleContinuityFinder,
)
from insouwiki.services.simple_convergence_finder import (
    SimpleConvergenceFinder,
)
from insouwiki.services.simple_divergence_finder import (
    SimpleDivergenceFinder,
)
from insouwiki.services.simple_documentary_question_interpreter import (
    SimpleDocumentaryQuestionInterpreter,
)
from insouwiki.services.simple_evolution_finder import (
    SimpleEvolutionFinder,
)
from insouwiki.services.simple_exploration_builder import (
    SimpleExplorationBuilder,
)
from insouwiki.services.simple_exploration_service import (
    SimpleExplorationService,
)


def test_reader_can_explore_documentary_sources_from_a_question():
    subject = DocumentarySubject(
        permanent_id="SUB-00000001",
        label="Retraites",
        documentary_expressions=(
            "retraite",
            "retraites",
        ),
    )

    exploration_service = SimpleExplorationService(
        SimpleExplorationBuilder(),
        SimpleDocumentaryQuestionInterpreter(
            subjects=[subject],
        ),
        SimpleContinuityFinder(),
        SimpleEvolutionFinder(),
        SimpleConvergenceFinder(),
        SimpleDivergenceFinder(),
    )

    question = DocumentaryQuestion(
        text=(
            "Que disent les sources "
            "sur la retraite à 60 ans ?"
        ),
    )

    exploration = exploration_service.explore(
        intent=ExplorationIntent.UNDERSTAND,
        question=question,
        facts=[],
    )

    search_service = Mock()
    search_service.search.return_value = [
        "résultat documentaire",
    ]

    executor = DocumentaryExplorationExecutor(
        search_service=search_service,
    )

    results = executor.execute(
        exploration,
    )

    assert exploration.subjects == [
        "Retraites",
    ]

    assert exploration.criteria == (
        DocumentaryCriterion(
            field="expression",
            value="60 ans",
        ),
    )

    search_service.search.assert_called_once_with(
        "60 ans",
    )

    assert results == [
        "résultat documentaire",
    ]
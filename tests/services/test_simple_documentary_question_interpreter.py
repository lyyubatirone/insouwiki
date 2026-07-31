from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.documentary_subject import (
    DocumentarySubject,
)
from insouwiki.services.simple_documentary_question_interpreter import (
    SimpleDocumentaryQuestionInterpreter,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.documentary_subject import (
    DocumentarySubject,
)
from insouwiki.services.simple_documentary_question_interpreter import (
    SimpleDocumentaryQuestionInterpreter,
)
from insouwiki.domain.documentary_personality import (
    DocumentaryPersonality,
)


def test_recognizes_known_documentary_subject():
    subject = DocumentarySubject(
        permanent_id="SUB-00000001",
        label="Retraites",
    )

    interpreter = SimpleDocumentaryQuestionInterpreter(
        subjects=[subject],
    )

    interpreted_subjects, interpreted_criteria = (
        interpreter.interpret(
            DocumentaryQuestion(
                text="Retraites",
            ),
        )
    )

    assert interpreted_subjects == [subject]
    assert interpreted_criteria == ()

def test_recognizes_subject_from_documentary_expression():
    subject = DocumentarySubject(
        permanent_id="SUB-00000001",
        label="Retraites",
        documentary_expressions=(
            "retraite",
            "retraites",
            "réforme des retraites",
        ),
    )

    interpreter = SimpleDocumentaryQuestionInterpreter(
        subjects=[subject],
    )

    interpreted_subjects, interpreted_criteria = (
        interpreter.interpret(
            DocumentaryQuestion(
                text=(
                    "Que disent les sources "
                    "sur les retraites ?"
                ),
            )
        )
    )

    assert interpreted_subjects == [subject]
    assert interpreted_criteria == ()

def test_extracts_expression_criterion_after_subject_recognition():
    subject = DocumentarySubject(
        permanent_id="SUB-00000001",
        label="Retraites",
        documentary_expressions=(
            "retraite",
            "retraites",
        ),
    )

    interpreter = SimpleDocumentaryQuestionInterpreter(
        subjects=[subject],
    )

    interpreted_subjects, interpreted_criteria = (
        interpreter.interpret(
            DocumentaryQuestion(
                text=(
                    "Que disent les sources "
                    "sur la retraite à 60 ans ?"
                ),
            ),
        )
    )

    assert interpreted_subjects == [subject]

    assert interpreted_criteria == (
        DocumentaryCriterion(
            field="expression",
            value="60 ans",
        ),
    )

def test_recognizes_documentary_personality():
    personality = DocumentaryPersonality(
        permanent_id="PER-00000001",
        slug="jean-luc-melenchon",
        display_name="Jean-Luc Mélenchon",
        documentary_expressions=(
            "Jean-Luc Mélenchon",
            "Mélenchon",
        ),
    )

    interpreter = SimpleDocumentaryQuestionInterpreter(
        subjects=[],
        personalities=[personality],
    )

    interpreted_subjects, interpreted_criteria = (
        interpreter.interpret(
            DocumentaryQuestion(
                text=(
                    "Que dit Jean-Luc Mélenchon "
                    "sur les retraites ?"
                ),
            ),
        )
    )

    assert interpreted_subjects == []

    assert interpreted_criteria == (
        DocumentaryCriterion(
            field="auteur",
            value="Jean-Luc Mélenchon",
        ),
    )
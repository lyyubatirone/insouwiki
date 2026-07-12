from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)


def test_documentary_question_keeps_original_text():
    question = DocumentaryQuestion(
        text=(
            "Que dit Jean-Luc Mélenchon "
            "sur la retraite à 60 ans ?"
        )
    )

    assert (
        question.text
        == (
            "Que dit Jean-Luc Mélenchon "
            "sur la retraite à 60 ans ?"
        )
    )


def test_documentary_question_is_immutable():
    question = DocumentaryQuestion(
        text="Retraite à 60 ans"
    )

    assert question.text == "Retraite à 60 ans"
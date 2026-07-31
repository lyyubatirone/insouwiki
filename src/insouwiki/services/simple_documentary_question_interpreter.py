import re
from insouwiki.domain.documentary_criterion import (
    DocumentaryCriterion,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.documentary_subject import (
    DocumentarySubject,
)
from insouwiki.services.documentary_question_interpreter import (
    DocumentaryQuestionInterpreter,
)
from insouwiki.domain.documentary_personality import (
    DocumentaryPersonality,
)

class SimpleDocumentaryQuestionInterpreter(
    DocumentaryQuestionInterpreter
):
    """
    Première interprétation documentaire par correspondance exacte.

    Cette implémentation reconnaît un sujet connu
    lorsque son libellé correspond exactement
    au texte de la question.
    """

    def __init__(
        self,
        subjects: list[DocumentarySubject],
        personalities: list[DocumentaryPersonality] | None = None,
    ) -> None:
        self._subjects = subjects
        self._personalities = (
            personalities
            if personalities is not None
            else []
        )

    def interpret(
        self,
        question: DocumentaryQuestion,
    ) -> tuple[
        list[DocumentarySubject],
        tuple[DocumentaryCriterion, ...],
    ]:
        interpreted_subjects: list[DocumentarySubject] = []
        interpreted_criteria: list[DocumentaryCriterion] = []

        for subject in self._subjects:
            if (
                subject.label.casefold()
                == question.text.strip().casefold()
            ):
                interpreted_subjects.append(subject)
                continue

            matching_expression = self._find_expression(
                question.text,
                subject.documentary_expressions,
            )

            if matching_expression is None:
                continue

            interpreted_subjects.append(subject)

            remaining_text = self._text_after_expression(
                question.text,
                matching_expression,
            )

            if remaining_text:
                interpreted_criteria.append(
                    DocumentaryCriterion(
                        field="expression",
                        value=remaining_text,
                    )
                )

        for personality in self._personalities:
            matching_expression = self._find_expression(
                question.text,
                personality.documentary_expressions,
            )

            if matching_expression is None:
                continue

            interpreted_criteria.append(
                DocumentaryCriterion(
                    field="auteur",
                    value=personality.display_name,
                )
            )

        return (
            interpreted_subjects,
            tuple(interpreted_criteria),
        )

    def _find_expression(
        self,
        question_text: str,
        expressions: tuple[str, ...],
    ) -> str | None:
        for expression in sorted(
            expressions,
            key=len,
            reverse=True,
        ):
            if re.search(
                rf"\b{re.escape(expression)}\b",
                question_text,
                flags=re.IGNORECASE,
            ):
                return expression

        return None

    def _text_after_expression(
        self,
        question_text: str,
        expression: str,
    ) -> str:
        match = re.search(
            rf"\b{re.escape(expression)}\b",
            question_text,
            flags=re.IGNORECASE,
        )

        if match is None:
            return ""

        remaining_text = question_text[
            match.end():
        ].strip(" \t\n\r,;:.!?")

        remaining_text = re.sub(
            r"^(à|au|aux|de|du|des|sur)\s+",
            "",
            remaining_text,
            flags=re.IGNORECASE,
        )

        return remaining_text.strip(
            " \t\n\r,;:.!?"
        )
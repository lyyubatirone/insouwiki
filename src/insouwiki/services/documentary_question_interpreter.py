from abc import ABC, abstractmethod

from insouwiki.domain.documentary_question import DocumentaryQuestion
from insouwiki.domain.documentary_subject import DocumentarySubject
from insouwiki.domain.documentary_criterion import DocumentaryCriterion


class DocumentaryQuestionInterpreter(ABC):
    """
    Interprète une question documentaire
    en sujets et critères documentaires.
    """

@abstractmethod
def interpret(
    self,
    question: DocumentaryQuestion,
) -> tuple[
    list[DocumentarySubject],
    tuple[DocumentaryCriterion, ...],
]:
    ...
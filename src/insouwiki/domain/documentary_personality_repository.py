from abc import ABC, abstractmethod

from insouwiki.domain.documentary_personality import (
    DocumentaryPersonality,
)


class DocumentaryPersonalityRepository(
    ABC,
):
    """
    Fournit les personnalités documentaires
    présentes dans le patrimoine documentaire.
    """

    @abstractmethod
    def list_all(
        self,
    ) -> list[DocumentaryPersonality]:
        """
        Retourne toutes les personnalités
        documentaires connues.
        """
from insouwiki.consultation.documentary_library import (
    DocumentaryLibrary,
)
from insouwiki.domain.documentary_clue import (
    DocumentaryClue,
)
from insouwiki.domain.investigation.investigation_state import (
    InvestigationState,
)
from insouwiki.web.services.search_service import (
    SearchService,
)


class InvestigationService:
    """
    Construit l'état d'une enquête documentaire
    et recherche ses pistes documentaires.
    """

    def __init__(
        self,
        documentary_library: DocumentaryLibrary | None = None,
        search_service: SearchService | None = None,
    ):
        self.documentary_library = (
            documentary_library
            if documentary_library is not None
            else DocumentaryLibrary()
        )
        self.search_service = (
            search_service
            if search_service is not None
            else SearchService()
        )

    def start(
        self,
        question: str,
        personality: str | None = None,
        personalities: list[str] | None = None,
    ) -> tuple[
        InvestigationState,
        list[DocumentaryClue],
    ]:
        state = InvestigationState(
            question=question,
        )

        if personality:
            state = state.with_personality(
                personality,
            )

        for current_personality in personalities or []:
            state = state.with_personality(
                current_personality,
            )

        results = self.search_service.search(
            question,
        )

        clues = [
            result
            for result in results
            if isinstance(result, DocumentaryClue)
        ]

        return state, clues

    def list_personalities(self):
        return self.documentary_library.list_personalities()
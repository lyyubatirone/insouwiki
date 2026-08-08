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
        context: str | None = None,
        document_type: str | None = None,
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
            normalized_personality = current_personality.strip()

            if not normalized_personality:
                continue

            state = state.with_personality(
                normalized_personality,
            )

        if context:
            state = state.with_context(
                context,
            )

        if document_type:
            state = state.with_document_type(
                document_type,
            )

        results = self.search_service.search(
            state,
        )

        clues = [
            result
            for result in results
            if isinstance(result, DocumentaryClue)
        ]

        return state, clues

    def list_personalities(self):
        return self.documentary_library.list_personalities()

    def list_contexts(self):
        return self.documentary_library.list_contexts()

    def list_document_types(self):
        return self.documentary_library.list_document_types()
from insouwiki.consultation.documentary_library import (
    DocumentaryLibrary,
)
from insouwiki.consultation.documentary_piece_view import (
    DocumentaryPieceView,
)
from insouwiki.domain.investigation.investigation_state import (
    InvestigationState,
)

class InvestigationService:
    """
    Construit l'état d'une enquête documentaire
    et recherche ses pièces documentaires.
    """

    def __init__(
        self,
        documentary_library: DocumentaryLibrary | None = None,
    ):
        self.documentary_library = (
            documentary_library
            if documentary_library is not None
            else DocumentaryLibrary()
        )

    def start(
        self,
        question: str,
        personality: str | None = None,
        personalities: list[str] | None = None,
    ) -> tuple[
        InvestigationState,
        list[DocumentaryPieceView],
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

        pieces = (
            self.documentary_library.search_documentary_pieces(
                question,
            )
        )

        return state, pieces
    
    def list_personalities(self):
                return self.documentary_library.list_personalities()
from datetime import date, timedelta

from insouwiki.domain.documentary_clue import (
    DocumentaryClue,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)
from insouwiki.domain.investigation.investigation_state import (
    InvestigationState,
)

class SearchService:
    """Fournit les résultats affichés sur la page de recherche."""

    def search(
        self,
        investigation: InvestigationState,
    ):
        normalized_query = (
            investigation.question
            .strip()
            .casefold()
        )
        
        if normalized_query == "jean-luc mélenchon":
            return [
                {
                    "label": "Jean-Luc Mélenchon",
                    "url": "/personnalites/jean-luc-melenchon",
                    "kind": "Personnalité",
                }
            ]

        if normalized_query == "retraite à 60 ans":
            results = [
                DocumentaryClue(
                    excerpt="La retraite doit être à 60 ans.",
                    speaker="Jean-Luc Mélenchon",
                    contexte="France Inter",
                    documentary_context="Campagne présidentielle 2022",
                    documentary_type="Interview",
                    document_id="SRC-00000001",
                    date=date(2022, 4, 12),
                    sequence_start=timedelta(
                        minutes=3,
                        seconds=17,
                    ),
                    sequence_end=timedelta(
                        minutes=3,
                        seconds=42,
                    ),
                    source_url=(
                        "https://www.youtube.com/watch"
                        "?v=WyjX4W0STmM"
                    ),
                ),
                DocumentaryClue(
                    excerpt=(
                        "Nous proposons le retour à la retraite "
                        "à 60 ans."
                    ),
                    speaker="Manuel Bompard",
                    contexte="Intervention publique",
                    documentary_context="XVIe législature (2022–2024)",
                    documentary_type="Discours",
                    document_id="SRC-00000001",
                    date=date(2023, 3, 16),
                    sequence_start=timedelta(
                        minutes=1,
                        seconds=8,
                    ),
                    sequence_end=timedelta(
                        minutes=1,
                        seconds=31,
                    ),
                    source_url=(
                        "https://www.youtube.com/watch"
                        "?v=WyjX4W0STmM"
                    ),
                ),
            ]

            if investigation.personalities:
                results = [
                    clue
                    for clue in results
                    if clue.speaker in investigation.personalities
                ]

            if investigation.context:
                results = [
                    clue
                    for clue in results
                    if clue.documentary_context
                    == investigation.context
                ]

            if investigation.document_type:
                results = [
                    clue
                    for clue in results
                    if clue.documentary_type
                    == investigation.document_type
                ]

            return results

        return []            

    def create_question(
        self,
        text: str,
    ) -> DocumentaryQuestion:
        return DocumentaryQuestion(
            text=text,
        )
    
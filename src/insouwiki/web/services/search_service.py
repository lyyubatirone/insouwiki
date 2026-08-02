from datetime import date, timedelta

from insouwiki.domain.documentary_clue import (
    DocumentaryClue,
)
from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)

class SearchService:
    """Fournit les résultats affichés sur la page de recherche."""

    def search(
        self,
        query: str,
    ):
        normalized_query = query.strip().casefold()

        if normalized_query == "jean-luc mélenchon":
            return [
                {
                    "label": "Jean-Luc Mélenchon",
                    "url": "/personnalites/jean-luc-melenchon",
                    "kind": "Personnalité",
                }
            ]

        if normalized_query == "retraite à 60 ans":
            return [
                DocumentaryClue(
                    excerpt="La retraite doit être à 60 ans.",
                    speaker="Jean-Luc Mélenchon",
                    contexte="France Inter",
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
            ]

        return []

    def create_question(
        self,
        text: str,
    ) -> DocumentaryQuestion:
        return DocumentaryQuestion(
            text=text,
        )
    
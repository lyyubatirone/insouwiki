from insouwiki.domain.documentary_question import (
    DocumentaryQuestion,
)


class SearchService:
    """Fournit les résultats affichés sur la page de recherche."""

    def search(
        self,
        query: str,
    ):
        if query.lower() == "jean-luc mélenchon":
            return [
                {
                    "label": "Jean-Luc Mélenchon",
                    "url": "/personnalites/jean-luc-melenchon",
                    "kind": "Personnalité",
                }
            ]

        return []

    def create_question(
        self,
        text: str,
    ) -> DocumentaryQuestion:
        return DocumentaryQuestion(
            text=text,
        )
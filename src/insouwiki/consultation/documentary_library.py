from insouwiki.consultation.document_view import DocumentView
from insouwiki.consultation.documentary_piece_view import DocumentaryPieceView
from insouwiki.consultation.personality_view import PersonalityView
from insouwiki.registry.postgres import PostgresDocumentRepository


class DocumentaryLibrary:
    """
    Bibliothèque documentaire de consultation.

    Point d'entrée des interfaces vers le patrimoine documentaire.
    """

    def __init__(
        self,
        document_repository: PostgresDocumentRepository | None = None,
    ):
        self.document_repository = (
            document_repository
            if document_repository is not None
            else PostgresDocumentRepository()
        )

    def get_personality(
        self,
        slug: str,
    ) -> PersonalityView:
        if slug == "jean-luc-melenchon":
            documents = self.document_repository.find_all()

            document_views = [
                DocumentView(
                    permanent_id=document.permanent_id,
                    title=document.title,
                    author=document.author,
                    original_url=str(document.original_url),
                )
                for document in documents[:10]
            ]

            first_document = document_views[0] if document_views else None

            return PersonalityView(
                name="Jean-Luc Mélenchon",
                description="Personnalité politique",
                document_count=self.document_repository.count(),
                documentary_piece_count=0,
                knowledge_count=0,
                relation_count=0,
                first_document=first_document,
                documents=document_views,
            )

        raise ValueError(f"Unknown personality: {slug}")

    def get_document(
        self,
        permanent_id: str,
    ) -> DocumentView:
        documents = self.document_repository.find_all()

        for document in documents:
            if document.permanent_id == permanent_id:
                return DocumentView(
                    permanent_id=document.permanent_id,
                    title=document.title,
                    author=document.author,
                    original_url=str(document.original_url),
                    documentary_pieces=self.get_documentary_pieces(
                        document.permanent_id
                    ),
                )

        raise ValueError(f"Unknown document: {permanent_id}")

       def get_documentary_pieces(
        self,
        document_permanent_id: str,
    ) -> list[DocumentaryPieceView]:
        """
        Retourne les pièces documentaires associées à un document.

        Implémentation provisoire : les pièces réelles seront raccordées
        lorsque le stockage des transcriptions et des séquences sera prêt.
        """
        return [
            DocumentaryPieceView(
                author="Jean-Luc Mélenchon",
                document_title="La nouvelle géopolitique de la France",
                sequence_text=(
                    "La retraite doit être à 60 ans pour tous."
                ),
                sequence_start="00:12:43",
                sequence_end="00:12:58",
                document_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            )
        ]
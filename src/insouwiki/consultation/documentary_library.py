from insouwiki.consultation.document_view import DocumentView
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

        # Premier document

            documents = self.document_repository.find_all()

            first_document = None

            if documents:
                document = documents[0]

                first_document = DocumentView(
                    title=document.title,
                    author=document.author,
                    original_url=str(document.original_url),
                )

            return PersonalityView(
                name="Jean-Luc Mélenchon",
                description="Personnalité politique",
                document_count=self.document_repository.count(),
                documentary_piece_count=0,
                knowledge_count=0,
                relation_count=0,
                first_document=first_document,
            )

        raise ValueError(f"Unknown personality: {slug}")
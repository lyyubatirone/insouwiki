from insouwiki.consultation.personality_view import PersonalityView


class DocumentaryLibrary:
    """
    Bibliothèque documentaire de consultation.

    Point d'entrée des interfaces vers le patrimoine documentaire.
    """

    def get_personality(
        self,
        slug: str,
    ) -> PersonalityView:
        if slug == "jean-luc-melenchon":
            return PersonalityView(
                name="Jean-Luc Mélenchon",
                description="Personnalité politique",
                document_count=2134,
                documentary_piece_count=0,
                knowledge_count=0,
                relation_count=0,
            )

        raise ValueError(f"Unknown personality: {slug}")
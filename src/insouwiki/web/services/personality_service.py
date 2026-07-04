from insouwiki.consultation.documentary_library import DocumentaryLibrary


class PersonalityService:
    """Fournit les informations affichées sur une fiche personnalité."""

    def __init__(
        self,
        documentary_library: DocumentaryLibrary | None = None,
    ):
        self.documentary_library = (
            documentary_library
            if documentary_library is not None
            else DocumentaryLibrary()
        )

    def get_personality(self, slug: str):
        return self.documentary_library.get_personality(slug)
class DocumentAvailabilityAnalyzer:
    """
    Détecte les documents qui ne sont plus observés
    lors d'une nouvelle synchronisation documentaire.
    """

    def detect_unavailable_documents(
        self,
        previous_documents: set[str],
        current_documents: set[str],
    ) -> set[str]:
        return previous_documents - current_documents
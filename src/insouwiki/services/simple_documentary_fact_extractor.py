from insouwiki.domain.documentary_fact import DocumentaryFact
from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.services.documentary_fact_extractor import (
    DocumentaryFactExtractor,
)


class SimpleDocumentaryFactExtractor(DocumentaryFactExtractor):
    """
    Première implémentation du générateur de faits documentaires.

    Version 1 :
    une séquence documentaire produit un fait documentaire.
    """

    def extract(
        self,
        sequences: list[DocumentarySequence],
    ) -> list[DocumentaryFact]:
        facts: list[DocumentaryFact] = []

        for index, sequence in enumerate(sequences, start=1):
            facts.append(
                DocumentaryFact(
                    permanent_id=f"FACT-{index:08d}",
                    author="Inconnu",
                    statement=sequence.text,
                    supporting_sequences=[sequence.permanent_id],
                )
            )

        return facts
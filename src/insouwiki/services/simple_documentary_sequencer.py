from datetime import timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.domain.transcription import Transcription
from insouwiki.services.documentary_sequencer import DocumentarySequencer


class SimpleDocumentarySequencer(DocumentarySequencer):
    """
    Séquenceur documentaire simple.

    Version 1 : transforme une transcription entière
    en une seule séquence documentaire.
    """

    def sequence(
        self,
        document: Document,
        transcription: Transcription,
    ) -> list[DocumentarySequence]:
        return [
            DocumentarySequence(
                permanent_id="SEQ-00000001",
                document_id=document.permanent_id or "document:unknown",
                start=timedelta(seconds=0),
                end=timedelta(seconds=0),
                text=transcription.text,
            )
        ]
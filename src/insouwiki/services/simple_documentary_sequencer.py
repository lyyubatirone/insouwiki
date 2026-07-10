from datetime import timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.domain.transcription import Transcription
from insouwiki.services.documentary_reasoning_analyzer import (
    DocumentaryReasoningAnalyzer,
)
from insouwiki.services.documentary_sequencer import DocumentarySequencer


class SimpleDocumentarySequencer(DocumentarySequencer):
    """
    Construit des séquences documentaires horodatées
    à partir des segments d'une transcription.

    Ces séquences constituent l'unité de recherche
    de la V1 d'InsouWiki.
    """

    def __init__(self):
        self._reasoning_analyzer = DocumentaryReasoningAnalyzer()

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

    def build_sequences(
        self,
        transcription,
    ) -> list[DocumentarySequence]:
        segments = transcription.segments

        if not segments:
            return []

        sequences = []
        current_segments = [segments[0]]

        for segment in segments[1:]:
            if self._reasoning_analyzer.belongs_to_same_reasoning(
                current_segments[-1],
                segment,
            ):
                current_segments.append(segment)
            else:
                sequences.append(
                    self._build_sequence(
                        transcription.document_id,
                        current_segments,
                        len(sequences) + 1,
                    )
                )
                current_segments = [segment]

        sequences.append(
            self._build_sequence(
                transcription.document_id,
                current_segments,
                len(sequences) + 1,
            )
        )

        return sequences

    def _build_sequence(
        self,
        document_id: str,
        segments,
        number: int,
    ) -> DocumentarySequence:
        return DocumentarySequence(
            permanent_id=f"SEQ-{number:08d}",
            document_id=document_id,
            start=segments[0].start,
            end=segments[-1].end,
            text="\n".join(
                segment.text
                for segment in segments
            ),
        )
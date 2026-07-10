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

    Pour la V1, chaque segment de transcription devient
    une séquence documentaire directement recherchable.

    La méthode build_sequences conserve la possibilité
    expérimentale de regrouper plusieurs segments selon
    la continuité d'un raisonnement documentaire.
    """

    def __init__(self) -> None:
        self._reasoning_analyzer = DocumentaryReasoningAnalyzer()

    def sequence(
        self,
        document: Document,
        transcription: Transcription,
    ) -> list[DocumentarySequence]:
        document_id = (
            document.permanent_id
            or transcription.document_id
            or "document:unknown"
        )

        if not transcription.segments:
            return [
                DocumentarySequence(
                    permanent_id="SEQ-00000001",
                    document_id=document_id,
                    start=timedelta(0),
                    end=timedelta(0),
                    text=transcription.text,
                )
            ]

        return [
            DocumentarySequence(
                permanent_id=f"SEQ-{index:08d}",
                document_id=document_id,
                start=segment.start,
                end=segment.end,
                text=segment.text,
            )
            for index, segment in enumerate(
                transcription.segments,
                start=1,
            )
        ]

    def build_sequences(
        self,
        transcription,
    ) -> list[DocumentarySequence]:
        segments = transcription.segments

        if not segments:
            return []

        sequences: list[DocumentarySequence] = []
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
                        document_id=transcription.document_id,
                        segments=current_segments,
                        number=len(sequences) + 1,
                    )
                )
                current_segments = [segment]

        sequences.append(
            self._build_sequence(
                document_id=transcription.document_id,
                segments=current_segments,
                number=len(sequences) + 1,
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
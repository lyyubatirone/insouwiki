from pathlib import Path

from insouwiki.domain.document import Document
from insouwiki.registry.sequence_repository import (
    DocumentarySequenceRepository,
)
from insouwiki.services.audio_extraction_service import (
    AudioExtractionService,
)
from insouwiki.services.document_indexer import DocumentIndexer
from insouwiki.services.documentary_sequencer import (
    DocumentarySequencer,
)
from insouwiki.services.transcription_service import (
    TranscriptionService,
)


class SimpleDocumentIndexer(DocumentIndexer):
    """
    Indexe un document en orchestrant l'extraction audio,
    la transcription, le séquençage et l'enregistrement
    des séquences documentaires.
    """

    def __init__(
        self,
        audio_extraction_service: AudioExtractionService,
        transcription_service: TranscriptionService,
        sequencer: DocumentarySequencer,
        sequence_repository: DocumentarySequenceRepository,
        audio_output_directory: Path,
    ) -> None:
        self._audio_extraction_service = audio_extraction_service
        self._transcription_service = transcription_service
        self._sequencer = sequencer
        self._sequence_repository = sequence_repository
        self._audio_output_directory = audio_output_directory

    def index(
        self,
        document: Document,
    ) -> None:
        extraction_result = self._audio_extraction_service.extract(
            document=document,
            output_directory=self._audio_output_directory,
        )

        transcription = self._transcription_service.transcribe(
            document=document,
            audio_path=extraction_result.audio_path,
        )

        sequences = self._sequencer.sequence(
            document=document,
            transcription=transcription,
        )

        self._sequence_repository.register_many(sequences)
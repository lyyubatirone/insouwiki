from pathlib import Path
from types import SimpleNamespace

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.domain.enums import DocumentKind
from insouwiki.services.simple_document_indexer import (
    SimpleDocumentIndexer,
)


class FakeAudioExtractionService:
    def __init__(self) -> None:
        self.extracted_document = None
        self.output_directory = None

    def extract(
        self,
        document: Document,
        output_directory: Path,
    ):
        self.extracted_document = document
        self.output_directory = output_directory

        return SimpleNamespace(
            audio_path=Path("tmp/audio/document.mp3"),
        )


class FakeTranscriptionService:
    def __init__(self) -> None:
        self.transcribed_document = None
        self.audio_path = None
        self.transcription = object()

    def transcribe(
        self,
        document: Document,
        audio_path: Path,
    ):
        self.transcribed_document = document
        self.audio_path = audio_path

        return self.transcription


class FakeDocumentarySequencer:
    def __init__(
        self,
        sequences: list[DocumentarySequence],
    ) -> None:
        self._sequences = sequences
        self.received_document = None
        self.received_transcription = None

    def sequence(
        self,
        document: Document,
        transcription,
    ) -> list[DocumentarySequence]:
        self.received_document = document
        self.received_transcription = transcription

        return self._sequences


class FakeDocumentarySequenceRepository:
    def __init__(self) -> None:
        self.registered_sequences = []
        self.deleted_document_id = None

    def register_many(
        self,
        sequences: list[DocumentarySequence],
    ) -> None:
        self.registered_sequences.extend(sequences)

    def delete_by_document(
        self,
        document_id: str,
    ) -> None:
        self.deleted_document_id = document_id


def test_indexes_document_and_registers_sequences():
    document = Document(
        permanent_id="DOC-00000001",
        origin_key="youtube:video:abc123",
        document_kind=DocumentKind.VIDEO,
        title="Document à indexer",
        original_url="https://www.youtube.com/watch?v=abc123",
    )

    expected_sequences = [
        DocumentarySequence(
            permanent_id="SEQ-00000001",
            document_id="DOC-00000001",
            start=0,
            end=10,
            text="Première séquence documentaire.",
        ),
        DocumentarySequence(
            permanent_id="SEQ-00000002",
            document_id="DOC-00000001",
            start=10,
            end=20,
            text="Deuxième séquence documentaire.",
        ),
    ]

    audio_extraction_service = FakeAudioExtractionService()
    transcription_service = FakeTranscriptionService()
    sequencer = FakeDocumentarySequencer(expected_sequences)
    sequence_repository = FakeDocumentarySequenceRepository()

    indexer = SimpleDocumentIndexer(
        audio_extraction_service=audio_extraction_service,
        transcription_service=transcription_service,
        sequencer=sequencer,
        sequence_repository=sequence_repository,
        audio_output_directory=Path("tmp/audio"),
    )

    indexer.index(document)

    assert audio_extraction_service.extracted_document == document
    assert audio_extraction_service.output_directory == Path("tmp/audio")

    assert transcription_service.transcribed_document == document
    assert transcription_service.audio_path == Path(
        "tmp/audio/document.mp3"
    )

    assert sequencer.received_document == document
    assert (
        sequencer.received_transcription
        is transcription_service.transcription
    )

    assert sequence_repository.registered_sequences == (
        expected_sequences
    )

    assert sequence_repository.deleted_document_id == "DOC-00000001"
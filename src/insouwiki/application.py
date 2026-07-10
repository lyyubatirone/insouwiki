from pathlib import Path

from insouwiki.registry.postgres import PostgresDocumentRepository
from insouwiki.registry.postgres_sequence_repository import (
    PostgresDocumentarySequenceRepository,
)
from insouwiki.services.audio_extraction_service import (
    AudioExtractionService,
)
from insouwiki.services.discovery_service import DiscoveryService
from insouwiki.services.documentary_search_service import (
    DocumentarySearchService,
)
from insouwiki.services.whisper_transcription_provider import (
    WhisperTranscriptionProvider,
)
from insouwiki.services.simple_document_indexer import (
    SimpleDocumentIndexer,
)
from insouwiki.services.simple_documentary_sequencer import (
    SimpleDocumentarySequencer,
)
from insouwiki.services.transcription_service import (
    TranscriptionService,
)
from insouwiki.services.youtube_audio_extractor import (
    YouTubeAudioExtractor,
)
from insouwiki.services.youtube_timestamp_link_builder import (
    YouTubeTimestampLinkBuilder,
)


class Application:
    """
    Point d'assemblage d'InsouWiki.

    Cette classe construit les services de l'application
    et leur fournit leurs dépendances.
    """

    def __init__(self) -> None:
        document_repository = PostgresDocumentRepository()
        sequence_repository = (
            PostgresDocumentarySequenceRepository()
        )

        self.document_repository = document_repository

        self.discovery_service = DiscoveryService(
            document_repository,
        )

        self.audio_extraction_service = AudioExtractionService(
            YouTubeAudioExtractor(),
        )

        self.transcription_service = TranscriptionService(
            WhisperTranscriptionProvider(),
        )

        self.document_indexer = SimpleDocumentIndexer(
            audio_extraction_service=(
                self.audio_extraction_service
            ),
            transcription_service=self.transcription_service,
            sequencer=SimpleDocumentarySequencer(),
            sequence_repository=sequence_repository,
            audio_output_directory=Path("tmp/audio"),
        )

        self.documentary_search_service = (
            DocumentarySearchService(
                document_repository=document_repository,
                sequence_repository=sequence_repository,
                timestamp_link_builder=(
                    YouTubeTimestampLinkBuilder()
                ),
            )
        )
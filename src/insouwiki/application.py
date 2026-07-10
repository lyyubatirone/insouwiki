from insouwiki.registry.postgres import PostgresDocumentRepository
from insouwiki.registry.postgres_sequence_repository import (
    PostgresDocumentarySequenceRepository,
)
from insouwiki.services.audio_extraction_service import AudioExtractionService
from insouwiki.services.discovery_service import DiscoveryService
from insouwiki.services.documentary_search_service import (
    DocumentarySearchService,
)
from insouwiki.services.dummy_transcription_provider import (
    DummyTranscriptionProvider,
)
from insouwiki.services.transcription_service import TranscriptionService
from insouwiki.services.youtube_audio_extractor import YouTubeAudioExtractor
from insouwiki.services.youtube_timestamp_link_builder import (
    YouTubeTimestampLinkBuilder,
)


class Application:
    """
    Point d'assemblage d'InsouWiki.

    Cette classe construit les services de l'application
    et leur fournit leurs dépendances.
    """

    def __init__(self):
        document_repository = PostgresDocumentRepository()
        sequence_repository = PostgresDocumentarySequenceRepository()

        self.discovery_service = DiscoveryService(document_repository)

        self.audio_extraction_service = AudioExtractionService(
            YouTubeAudioExtractor()
        )

        self.transcription_service = TranscriptionService(
            DummyTranscriptionProvider()
        )

        self.documentary_search_service = DocumentarySearchService(
            document_repository=document_repository,
            sequence_repository=sequence_repository,
            timestamp_link_builder=YouTubeTimestampLinkBuilder(),
        )
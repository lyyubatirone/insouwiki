from insouwiki.registry.postgres import PostgresDocumentRepository
from insouwiki.services.audio_extraction_service import AudioExtractionService
from insouwiki.services.discovery_service import DiscoveryService
from insouwiki.services.transcription_service import TranscriptionService
from insouwiki.services.youtube_audio_extractor import YouTubeAudioExtractor
from insouwiki.services.dummy_transcription_provider import (
    DummyTranscriptionProvider,
)


class Application:
    """
    Point d'assemblage d'InsouWiki.

    Cette classe construit les services de l'application
    et leur fournit leurs dépendances.
    """

    def __init__(self):
        repository = PostgresDocumentRepository()

        self.discovery_service = DiscoveryService(repository)

        self.audio_extraction_service = AudioExtractionService(
            YouTubeAudioExtractor()
        )

        self.transcription_service = TranscriptionService(
            DummyTranscriptionProvider()
        )
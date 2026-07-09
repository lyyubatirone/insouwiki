from insouwiki.application import Application
from insouwiki.services.audio_extraction_service import AudioExtractionService
from insouwiki.services.discovery_service import DiscoveryService
from insouwiki.services.transcription_service import TranscriptionService


def test_application_builds_services():
    application = Application()

    assert isinstance(application.discovery_service, DiscoveryService)
    assert isinstance(application.audio_extraction_service, AudioExtractionService)
    assert isinstance(application.transcription_service, TranscriptionService)
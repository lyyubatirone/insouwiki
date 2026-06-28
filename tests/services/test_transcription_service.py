from insouwiki.domain.document import Document
from insouwiki.domain.enums import DocumentKind
from insouwiki.services.dummy_transcription_provider import DummyTranscriptionProvider
from insouwiki.services.transcription_service import TranscriptionService


def test_transcription_service_uses_provider():
    document = Document(
        permanent_id="SRC-00000001",
        origin_key="youtube:test-video",
        document_kind=DocumentKind.VIDEO,
        title="Vidéo de test",
        original_url="https://www.youtube.com/watch?v=test-video",
    )

    provider = DummyTranscriptionProvider()
    service = TranscriptionService(provider)

    transcription = service.transcribe(document)

    assert transcription.document_id == "SRC-00000001"
    assert transcription.language == "fr"
    assert transcription.text == "Ceci est une transcription de démonstration."
    assert transcription.engine == "dummy"
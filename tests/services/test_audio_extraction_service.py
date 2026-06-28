from insouwiki.domain.document import Document
from insouwiki.domain.enums import DocumentKind
from insouwiki.services.audio_extraction_service import AudioExtractionService
from insouwiki.services.dummy_audio_extractor import DummyAudioExtractor


def test_audio_extraction_service_uses_extractor(tmp_path):
    document = Document(
        permanent_id="SRC-00000001",
        origin_key="youtube:test-video",
        document_kind=DocumentKind.VIDEO,
        title="Vidéo de test",
        original_url="https://www.youtube.com/watch?v=test-video",
    )

    extractor = DummyAudioExtractor()
    service = AudioExtractionService(extractor)

    audio_path = service.extract(
        document=document,
        output_directory=tmp_path,
    )

    assert audio_path.exists()
    assert audio_path.read_text(encoding="utf-8") == "Audio factice pour SRC-00000001"
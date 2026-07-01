from pathlib import Path

from insouwiki.domain.document import Document
from insouwiki.domain.enums import DocumentKind
from insouwiki.services.openai_transcription_provider import OpenAITranscriptionProvider


audio_path = Path("tmp/audio/6ruS-hrujhI.m4a")

document = Document(
    permanent_id="document:manual",
    origin_key="manual:6ruS-hrujhI",
    document_kind=DocumentKind.VIDEO,
    title="Document manuel",
    original_url="https://www.youtube.com/watch?v=6ruS-hrujhI",
)

provider = OpenAITranscriptionProvider()

transcription = provider.transcribe(
    document=document,
    audio_path=audio_path,
)

print("✓ Transcription réalisée")
print(f"Document : {transcription.document_id}")
print(f"Moteur   : {transcription.engine}")
print()
print(transcription.text[:1000])
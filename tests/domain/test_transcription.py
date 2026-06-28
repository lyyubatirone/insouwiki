from insouwiki.domain.transcription import Transcription


def test_create_transcription():
    transcription = Transcription(
        document_id="SRC-00000001",
        language="fr",
        text="Bonjour tout le monde.",
        engine="manual",
    )

    assert transcription.document_id == "SRC-00000001"
    assert transcription.language == "fr"
    assert transcription.text == "Bonjour tout le monde."
    assert transcription.engine == "manual"
    assert transcription.permanent_id is None
    assert transcription.created_at is not None
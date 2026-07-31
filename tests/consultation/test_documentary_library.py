from insouwiki.domain.documentary_sequence import (
    DocumentarySequence,
)
from insouwiki.domain.documentary_personality import (
    DocumentaryPersonality,
)
from insouwiki.services.simple_documentary_personality_repository import (
    SimpleDocumentaryPersonalityRepository,
)
from insouwiki.consultation.documentary_library import (
    DocumentaryLibrary,
)
from insouwiki.domain.document import Document

from insouwiki.domain.transcription import Transcription

from datetime import timedelta

from insouwiki.domain.transcription import (
    Transcription,
)
from insouwiki.domain.transcription_segment import (
    TranscriptionSegment,
)

from insouwiki.consultation.documentary_fact_view import (
    DocumentaryFactView,
)

class InMemoryDocumentRepository:
    def __init__(
        self,
        documents: list[Document],
    ):
        self.documents = documents

    def find_all(
        self,
    ) -> list[Document]:
        return self.documents
    
class InMemoryTranscriptionRepository:
    def __init__(
        self,
        transcriptions: list[Transcription],
    ):
        self.transcriptions = transcriptions

    def find_by_document(
        self,
        document_permanent_id: str,
    ) -> Transcription | None:
        for transcription in self.transcriptions:
            if (
                transcription.document_id
                == document_permanent_id
            ):
                return transcription

        return None
    
class InMemoryDocumentarySequenceRepository:
    def __init__(
        self,
        sequences: list[DocumentarySequence],
    ):
        self.sequences = sequences

    def find_by_document(
        self,
        document_permanent_id: str,
    ) -> list[DocumentarySequence]:
        return [
            sequence
            for sequence in self.sequences
            if sequence.document_id
            == document_permanent_id
        ]

def test_lists_documentary_personalities():
    documents = [
        Document(
            origin_key="1",
            document_kind="video",
            title="Discours",
            original_url="https://example.com/video",
            author="Jean-Luc Mélenchon",
        ),
    ]

    library = DocumentaryLibrary(
        personality_repository=(
            SimpleDocumentaryPersonalityRepository(
                documents,
            )
        ),
    )

    personalities = library.list_personalities()

    assert personalities == [
        DocumentaryPersonality(
            permanent_id="PER-00000001",
            slug="jean-luc-melenchon",
            display_name="Jean-Luc Mélenchon",
            document_count=1,
        ),
    ]

def test_lists_documents_for_personality():
    documents = [
        Document(
            origin_key="1",
            document_kind="video",
            title="Discours 1",
            original_url="https://a",
            author="Jean-Luc Mélenchon",
        ),
        Document(
            origin_key="2",
            document_kind="video",
            title="Discours 2",
            original_url="https://b",
            author="Manuel Bompard",
        ),
    ]

    library = DocumentaryLibrary(
        document_repository=InMemoryDocumentRepository(
            documents,
        ),
    )

    result = library.documents_for_personality(
        "jean-luc-melenchon",
    )

    assert len(result) == 1
    assert result[0].title == "Discours 1"

def test_returns_none_when_document_has_no_transcription():
    library = DocumentaryLibrary()

    assert (
        library.get_transcription(
            "SRC-00003151",
        )
        is None
    )

def test_returns_existing_transcription():
    transcription = Transcription(
        permanent_id="TRS-00000001",
        document_id="SRC-00000001",
        language="fr",
        text="Bonjour à toutes et à tous.",
        engine="test",
    )

    library = DocumentaryLibrary(
        transcription_repository=(
            InMemoryTranscriptionRepository(
                [transcription],
            )
        ),
    )

    result = library.get_transcription(
        "SRC-00000001",
    )

    assert result == transcription

def test_returns_transcription_with_segments():
    transcription = Transcription(
        permanent_id="TRS-00000001",
        document_id="SRC-00000001",
        language="fr",
        text="Bonjour à toutes et à tous.",
        engine="test",
        segments=[
            TranscriptionSegment(
                start=timedelta(seconds=0),
                end=timedelta(seconds=5),
                speaker="Jean-Luc Mélenchon",
                text="Bonjour à toutes et à tous.",
            ),
        ],
    )

    library = DocumentaryLibrary(
        transcription_repository=(
            InMemoryTranscriptionRepository(
                [transcription],
            )
        ),
    )

    result = library.get_transcription(
        "SRC-00000001",
    )

    assert result is not None

    assert len(result.segments) == 1

    assert (
        result.segments[0].text
        == "Bonjour à toutes et à tous."
    )

def test_returns_documentary_sequences_for_document():
    sequence = DocumentarySequence(
        permanent_id="SEQ-00000001",
        document_id="SRC-00000001",
        start=timedelta(seconds=0),
        end=timedelta(seconds=10),
        text="La retraite à 60 ans est une nécessité.",
    )

    library = DocumentaryLibrary(
        sequence_repository=(
            InMemoryDocumentarySequenceRepository(
                [sequence],
            )
        ),
    )

    result = library.get_sequences(
        "SRC-00000001",
    )

    assert result == [sequence]

def test_returns_documentary_facts_for_document():
    sequence = DocumentarySequence(
        permanent_id="SEQ-00000001",
        document_id="SRC-00000001",
        start=timedelta(seconds=0),
        end=timedelta(seconds=10),
        text="La retraite à 60 ans est une nécessité.",
    )

    library = DocumentaryLibrary(
        sequence_repository=(
            InMemoryDocumentarySequenceRepository(
                [sequence],
            )
        ),
    )

    facts = library.get_documentary_facts(
        "SRC-00000001",
    )

    assert len(facts) == 1
    assert facts[0].statement == (
        "La retraite à 60 ans est une nécessité."
    )

def test_returns_documentary_fact_views_for_document():
    sequence = DocumentarySequence(
        permanent_id="SEQ-00000001",
        document_id="SRC-00000001",
        start=timedelta(seconds=10),
        end=timedelta(seconds=20),
        text="La retraite à 60 ans est une nécessité.",
    )

    library = DocumentaryLibrary(
        sequence_repository=(
            InMemoryDocumentarySequenceRepository(
                [sequence],
            )
        ),
    )

    result = library.get_documentary_fact_views(
        "SRC-00000001",
    )

    assert result == [
        DocumentaryFactView(
            author="JEAN-LUC MÉLENCHON",
            statement=(
                "La retraite à 60 ans est une nécessité."
            ),
            source_sequence_id="SEQ-00000001",
            source_start="0:00:10",
            source_end="0:00:20",
            source_url=(
                "https://www.youtube.com/watch?v=7F8wvt4QxoE&t=10s"
            ),
        ),
    ]

    assert result[0].source_url == (
        "https://www.youtube.com/watch"
        "?v=7F8wvt4QxoE&t=10s"
    )
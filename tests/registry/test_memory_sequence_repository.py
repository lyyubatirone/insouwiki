from datetime import timedelta

from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.registry.memory_sequence_repository import (
    MemoryDocumentarySequenceRepository,
)


def test_memory_sequence_repository_finds_sequences_by_document():
    repository = MemoryDocumentarySequenceRepository()

    first_sequence = DocumentarySequence(
        permanent_id="SEQ-000001",
        document_id="DOC-000001",
        start=timedelta(seconds=10),
        end=timedelta(seconds=20),
        text="Première séquence documentaire.",
    )

    second_sequence = DocumentarySequence(
        permanent_id="SEQ-000002",
        document_id="DOC-000001",
        start=timedelta(seconds=30),
        end=timedelta(seconds=40),
        text="Deuxième séquence documentaire.",
    )

    repository.register_many(
        [
            first_sequence,
            second_sequence,
        ]
    )

    sequences = repository.find_by_document("DOC-000001")

    assert sequences == [
        first_sequence,
        second_sequence,
    ]


def test_memory_sequence_repository_returns_empty_list_for_unknown_document():
    repository = MemoryDocumentarySequenceRepository()

    sequence = DocumentarySequence(
        permanent_id="SEQ-000001",
        document_id="DOC-000001",
        start=timedelta(seconds=10),
        end=timedelta(seconds=20),
        text="Séquence documentaire.",
    )

    repository.register_many([sequence])

    sequences = repository.find_by_document("DOC-999999")

    assert sequences == []
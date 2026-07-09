from datetime import timedelta

from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.registry.postgres_sequence_repository import (
    PostgresDocumentarySequenceRepository,
)


def test_postgres_sequence_repository_registers_and_finds_sequences():
    repository = PostgresDocumentarySequenceRepository()

    sequence = DocumentarySequence(
        permanent_id="SEQ-TEST-000001",
        document_id="SRC-00000001",
        start=timedelta(seconds=10),
        end=timedelta(seconds=20),
        text="Séquence documentaire de test.",
    )

    repository.register_many([sequence])

    sequences = repository.find_by_document("SRC-00000001")

    assert sequence in sequences
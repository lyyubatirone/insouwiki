from datetime import timedelta

from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.registry.postgres_sequence_repository import (
    PostgresDocumentarySequenceRepository,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
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

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documentary_sequences
                WHERE permanent_id = %s
                """,
                (sequence.permanent_id,),
            )

        conn.commit()

def test_postgres_sequence_repository_assigns_permanent_id():
    repository = PostgresDocumentarySequenceRepository()

    sequence = DocumentarySequence(
        permanent_id=None,
        document_id="SRC-00000836",
        start=timedelta(seconds=5),
        end=timedelta(seconds=14),
        text=(
            "Il faut choisir entre ceux qui veulent nous faire "
            "partir toujours plus tard et celui qui propose "
            "la retraite à 60 ans avec 40 annuités de cotisation."
        ),
    )

    repository.register_many(
        [sequence],
    )

    assert sequence.permanent_id is not None
    assert sequence.permanent_id.startswith("SEQ-")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documentary_sequences
                WHERE permanent_id = %s
                """,
                (sequence.permanent_id,),
            )

        conn.commit()


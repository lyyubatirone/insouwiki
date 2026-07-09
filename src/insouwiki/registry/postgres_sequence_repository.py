from datetime import timedelta

from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.registry.postgres_connection import get_connection
from insouwiki.registry.sequence_repository import (
    DocumentarySequenceRepository,
)


class PostgresDocumentarySequenceRepository(
    DocumentarySequenceRepository
):

    def register_many(
        self,
        sequences: list[DocumentarySequence],
    ) -> None:
        if not sequences:
            return

        with get_connection() as conn:
            with conn.cursor() as cur:
                for sequence in sequences:
                    cur.execute(
                        """
                        INSERT INTO documentary_sequences (
                            permanent_id,
                            document_id,
                            start_seconds,
                            end_seconds,
                            text
                        )
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (permanent_id) DO NOTHING
                        """,
                        (
                            sequence.permanent_id,
                            sequence.document_id,
                            int(sequence.start.total_seconds()),
                            int(sequence.end.total_seconds()),
                            sequence.text,
                        ),
                    )

            conn.commit()

    def find_by_document(
        self,
        document_id: str,
    ) -> list[DocumentarySequence]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        document_id,
                        start_seconds,
                        end_seconds,
                        text
                    FROM documentary_sequences
                    WHERE document_id = %s
                    """,
                    (document_id,),
                )

                rows = cur.fetchall()

                return [
                    DocumentarySequence(
                        permanent_id=row[0],
                        document_id=row[1],
                        start=timedelta(seconds=row[2]),
                        end=timedelta(seconds=row[3]),
                        text=row[4],
                    )
                    for row in rows
                ]
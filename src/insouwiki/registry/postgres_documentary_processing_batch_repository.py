from datetime import timedelta

from insouwiki.domain.documentary_processing_batch import (
    DocumentaryProcessingBatch,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
)


class PostgresDocumentaryProcessingBatchRepository:
    def register(
        self,
        batch: DocumentaryProcessingBatch,
    ) -> DocumentaryProcessingBatch:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if batch.permanent_id is None:
                    cur.execute(
                        """
                        SELECT permanent_id
                        FROM documentary_processing_batches
                        WHERE permanent_id ~ '^BATCH-[0-9]{8}$'
                        ORDER BY permanent_id DESC
                        LIMIT 1
                        """
                    )

                    row = cur.fetchone()

                    if row is None:
                        next_id = 1
                    else:
                        next_id = int(
                            row[0].removeprefix(
                                "BATCH-"
                            )
                        ) + 1

                    permanent_id = (
                        f"BATCH-{next_id:08d}"
                    )
                else:
                    permanent_id = batch.permanent_id

                cur.execute(
                    """
                    INSERT INTO documentary_processing_batches (
                        permanent_id,
                        name,
                        status
                    )
                    VALUES (%s, %s, %s)
                    """,
                    (
                        permanent_id,
                        batch.name,
                        batch.status,
                    ),
                )

                for document_id in batch.document_ids:
                    cur.execute(
                        """
                        INSERT INTO
                            documentary_processing_batch_documents (
                                batch_id,
                                document_id
                            )
                        VALUES (%s, %s)
                        """,
                        (
                            permanent_id,
                            document_id,
                        ),
                    )

            conn.commit()

        return DocumentaryProcessingBatch(
            permanent_id=permanent_id,
            name=batch.name,
            document_ids=list(
                batch.document_ids
            ),
            document_durations=list(
                batch.document_durations
            ),
            status=batch.status,
        )

    def update_status(
        self,
        batch: DocumentaryProcessingBatch,
    ) -> None:
        if batch.permanent_id is None:
            raise ValueError(
                "Cannot update a processing batch "
                "without a permanent identifier."
            )

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE documentary_processing_batches
                    SET
                        status = %s,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE permanent_id = %s
                    """,
                    (
                        batch.status,
                        batch.permanent_id,
                    ),
                )

            conn.commit()

    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> DocumentaryProcessingBatch | None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        name,
                        status
                    FROM documentary_processing_batches
                    WHERE permanent_id = %s
                    """,
                    (permanent_id,),
                )

                batch_row = cur.fetchone()

                if batch_row is None:
                    return None

                cur.execute(
                    """
                    SELECT
                        d.permanent_id,
                        d.duration_seconds
                    FROM documentary_processing_batch_documents AS b
                    JOIN documents AS d
                        ON d.permanent_id = b.document_id
                    WHERE b.batch_id = %s
                    ORDER BY d.permanent_id
                    """,
                    (permanent_id,),
                )

                document_rows = cur.fetchall()

        document_ids = [
            row[0]
            for row in document_rows
        ]

        document_durations = [
            timedelta(seconds=row[1])
            for row in document_rows
            if row[1] is not None
        ]

        return DocumentaryProcessingBatch(
            permanent_id=batch_row[0],
            name=batch_row[1],
            status=batch_row[2],
            document_ids=document_ids,
            document_durations=document_durations,
        )
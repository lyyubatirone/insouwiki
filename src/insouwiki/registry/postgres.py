from datetime import timedelta

from insouwiki.domain.document import Document
from insouwiki.domain.enums import (
    DocumentaryNature,
    ProcessingStatus,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
)
from insouwiki.registry.repository import DocumentRepository
from insouwiki.registry.result import RegistrationResult


class PostgresDocumentRepository(DocumentRepository):

    def exists(self, origin_key: str) -> bool:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT 1
                    FROM documents
                    WHERE origin_key = %s
                    """,
                    (origin_key,),
                )

                return cur.fetchone() is not None

    def count(self) -> int:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT COUNT(*) FROM documents"
                )

                return cur.fetchone()[0]

    def find_all(self) -> list[Document]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        source_permanent_id,
                        discovered_from_endpoint_permanent_id,
                        origin_key,
                        document_kind,
                        title,
                        original_url,
                        source_platform,
                        external_id,
                        author,
                        published_at,
                        duration_seconds,
                        thumbnail_url,
                        documentary_nature,
                        status
                    FROM documents
                    """
                )

                rows = cur.fetchall()

                return [
                    self._build_document(row)
                    for row in rows
                ]

    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> Document | None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        source_permanent_id,
                        discovered_from_endpoint_permanent_id,
                        origin_key,
                        document_kind,
                        title,
                        original_url,
                        source_platform,
                        external_id,
                        author,
                        published_at,
                        duration_seconds,
                        thumbnail_url,
                        documentary_nature,
                        status
                    FROM documents
                    WHERE permanent_id = %s
                    """,
                    (permanent_id,),
                )

                row = cur.fetchone()

                if row is None:
                    return None

                return self._build_document(row)

    def get_by_original_url(
        self,
        original_url: str,
    ) -> Document | None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        source_permanent_id,
                        discovered_from_endpoint_permanent_id,
                        origin_key,
                        document_kind,
                        title,
                        original_url,
                        source_platform,
                        external_id,
                        author,
                        published_at,
                        duration_seconds,
                        thumbnail_url,
                        documentary_nature,
                        status
                    FROM documents
                    WHERE original_url = %s
                    """,
                    (original_url,),
                )

                row = cur.fetchone()

                if row is None:
                    return None

                return self._build_document(row)

    def register(
        self,
        document: Document,
    ) -> RegistrationResult:
        return self.register_many([document])[0]

    def register_many(
        self,
        documents: list[Document],
    ) -> list[RegistrationResult]:
        if not documents:
            return []

        results: list[RegistrationResult] = []

        origin_keys = [
            document.origin_key
            for document in documents
        ]

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        origin_key,
                        permanent_id
                    FROM documents
                    WHERE origin_key = ANY(%s)
                    """,
                    (origin_keys,),
                )

                existing = {
                    origin_key: permanent_id
                    for origin_key, permanent_id
                    in cur.fetchall()
                }

                cur.execute(
                    """
                    SELECT permanent_id
                    FROM documents
                    WHERE permanent_id ~ '^SRC-[0-9]{8}$'
                    ORDER BY permanent_id DESC
                    LIMIT 1
                    """
                )

                row = cur.fetchone()

                if row is None:
                    next_id = 1
                else:
                    next_id = int(
                        row[0].removeprefix("SRC-")
                    ) + 1

                for document in documents:
                    if document.origin_key in existing:
                        document.permanent_id = existing[
                            document.origin_key
                        ]

                        if document.duration is not None:
                            cur.execute(
                                """
                                UPDATE documents
                                SET duration_seconds = %s
                                WHERE origin_key = %s
                                """,
                                (
                                    int(
                                        document.duration.total_seconds()
                                    ),
                                    document.origin_key,
                                ),
                            )

                        results.append(
                            RegistrationResult(
                                document_id=(
                                    document.permanent_id
                                ),
                                created=False,
                            )
                        )

                        continue

                    document.permanent_id = (
                        f"SRC-{next_id:08d}"
                    )
                    next_id += 1

                    cur.execute(
                        """
                        INSERT INTO documents (
                            permanent_id,
                            source_permanent_id,
                            discovered_from_endpoint_permanent_id,
                            origin_key,
                            document_kind,
                            title,
                            author,
                            original_url,
                            source_platform,
                            external_id,
                            published_at,
                            duration_seconds,
                            thumbnail_url,
                            documentary_nature,
                            status,
                            metadata
                        )
                        VALUES (
                            %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s,
                            %s
                        )
                        """,
                        (
                            document.permanent_id,
                            document.source_permanent_id,
                            (
                                document
                                .discovered_from_endpoint_permanent_id
                            ),
                            document.origin_key,
                            document.document_kind.value,
                            document.title,
                            document.author,
                            str(document.original_url),
                            document.source_platform,
                            document.external_id,
                            document.published_at,
                            (
                                int(
                                    document
                                    .duration
                                    .total_seconds()
                                )
                                if document.duration
                                is not None
                                else None
                            ),
                            (
                                str(document.thumbnail_url)
                                if document.thumbnail_url
                                else None
                            ),
                            document.documentary_nature.value,
                            document.status.value,
                            "{}",
                        ),
                    )

                    results.append(
                        RegistrationResult(
                            document_id=(
                                document.permanent_id
                            ),
                            created=True,
                        )
                    )

            conn.commit()

        return results

    def update_status(
        self,
        origin_key: str,
        status: ProcessingStatus,
    ) -> None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE documents
                    SET status = %s
                    WHERE origin_key = %s
                    """,
                    (
                        status.value,
                        origin_key,
                    ),
                )

            conn.commit()

    def _build_document(
        self,
        row,
    ) -> Document:
        return Document(
            permanent_id=row[0],
            source_permanent_id=row[1],
            discovered_from_endpoint_permanent_id=row[2],
            origin_key=row[3],
            document_kind=row[4],
            title=row[5],
            original_url=row[6],
            source_platform=row[7],
            external_id=row[8],
            author=row[9],
            published_at=row[10],
            duration=(
                timedelta(seconds=row[11])
                if row[11] is not None
                else None
            ),
            thumbnail_url=row[12],
            documentary_nature=(
                row[13]
                or DocumentaryNature.PRIMARY
            ),
            status=(
                row[14]
                or ProcessingStatus.DISCOVERED
            ),
        )
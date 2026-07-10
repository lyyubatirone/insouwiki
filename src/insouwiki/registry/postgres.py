from insouwiki.domain.document import Document
from insouwiki.registry.postgres_connection import get_connection
from insouwiki.registry.repository import DocumentRepository
from insouwiki.registry.result import RegistrationResult
from insouwiki.domain.enums import DocumentaryNature, ProcessingStatus


class PostgresDocumentRepository(DocumentRepository):

    def exists(self, origin_key: str) -> bool:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT 1 FROM documents WHERE origin_key = %s",
                    (origin_key,),
                )
                return cur.fetchone() is not None

    def count(self) -> int:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM documents")
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
                        thumbnail_url,
                        documentary_nature,
                        status
                    FROM documents
                    """
                )

                return [
                    Document(
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
                        thumbnail_url=row[11],
                        documentary_nature=row[12] or DocumentaryNature.PRIMARY,
                        status=row[13] or ProcessingStatus.DISCOVERED,                    )
                    for row in cur.fetchall()
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
                    thumbnail_url=row[11],
                    documentary_nature=(
                        row[12] or DocumentaryNature.PRIMARY
                    ),
                    status=(
                        row[13] or ProcessingStatus.DISCOVERED
                    ),
                )

    def register(self, document: Document) -> RegistrationResult:
        return self.register_many([document])[0]

    def register_many(self, documents: list[Document]) -> list[RegistrationResult]:
        if not documents:
            return []

        results: list[RegistrationResult] = []
        origin_keys = [document.origin_key for document in documents]

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT origin_key, permanent_id
                    FROM documents
                    WHERE origin_key = ANY(%s)
                    """,
                    (origin_keys,),
                )

                existing = {
                    origin_key: permanent_id
                    for origin_key, permanent_id in cur.fetchall()
                }

                cur.execute("SELECT COUNT(*) FROM documents")
                next_id = cur.fetchone()[0] + 1

                for document in documents:
                    if document.origin_key in existing:
                        document.permanent_id = existing[document.origin_key]
                        results.append(
                            RegistrationResult(
                                document_id=document.permanent_id,
                                created=False,
                            )
                        )
                        continue

                    document.permanent_id = f"SRC-{next_id:08d}"
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
                            thumbnail_url,
                            documentary_nature,
                            status,
                            metadata
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            document.permanent_id,
                            document.source_permanent_id,
                            document.discovered_from_endpoint_permanent_id,
                            document.origin_key,
                            document.document_kind.value,
                            document.title,
                            document.author,
                            str(document.original_url),
                            document.source_platform,
                            document.external_id,
                            document.published_at,
                            str(document.thumbnail_url)
                            if document.thumbnail_url
                            else None,
                            document.documentary_nature.value,
                            document.status.value,
                            "{}",
                        ),
                    )

                    results.append(
                        RegistrationResult(
                            document_id=document.permanent_id,
                            created=True,
                        )
                    )

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
                    thumbnail_url=row[11],
                    documentary_nature=(
                        row[12] or DocumentaryNature.PRIMARY
                    ),
                    status=(
                        row[13] or ProcessingStatus.DISCOVERED
                    ),
                )
            conn.commit()

        return results
    

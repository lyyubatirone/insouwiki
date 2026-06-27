from insouwiki.domain.models import Document
from insouwiki.registry.postgres_connection import get_connection
from insouwiki.registry.repository import DocumentRepository
from insouwiki.registry.result import RegistrationResult


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
                            origin_key,
                            document_kind,
                            title,
                            author,
                            original_url
                        )
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        (
                            document.permanent_id,
                            document.origin_key,
                            document.document_kind.value,
                            document.title,
                            document.author,
                            str(document.original_url),
                        ),
                    )

                    results.append(
                        RegistrationResult(
                            document_id=document.permanent_id,
                            created=True,
                        )
                    )

            conn.commit()

        return results
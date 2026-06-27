from insouwiki.domain.models import Document
from insouwiki.registry.postgres_connection import get_connection
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
                cur.execute("SELECT COUNT(*) FROM documents")
                return cur.fetchone()[0]

    def register(self, document: Document) -> RegistrationResult:

        if self.exists(document.origin_key):
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT permanent_id
                        FROM documents
                        WHERE origin_key = %s
                        """,
                        (document.origin_key,),
                    )

                    permanent_id = cur.fetchone()[0]

            return RegistrationResult(
                document_id=permanent_id,
                created=False,
            )

        document.permanent_id = f"SRC-{self.count() + 1:08d}"

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO documents
                    (
                        permanent_id,
                        origin_key,
                        document_kind,
                        title,
                        author,
                        original_url
                    )
                    VALUES
                    (%s, %s, %s, %s, %s, %s)
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

            conn.commit()

        return RegistrationResult(
            document_id=document.permanent_id,
            created=True,
        )
from insouwiki.domain.source import DocumentSourceRecord
from insouwiki.registry.postgres_connection import get_connection


class SourceRepository:

    def count(self) -> int:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM sources")
                return cur.fetchone()[0]

    def register(self, source: DocumentSourceRecord) -> DocumentSourceRecord:

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT permanent_id
                    FROM sources
                    WHERE url = %s
                    """,
                    (str(source.url),),
                )

                existing = cur.fetchone()

                if existing:
                    source.permanent_id = existing[0]
                    return source

                source.permanent_id = f"SRC-SOURCE-{self.count() + 1:06d}"

                cur.execute(
                    """
                    INSERT INTO sources (
                        permanent_id,
                        source_kind,
                        name,
                        url,
                        external_id,
                        status
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (
                        source.permanent_id,
                        source.source_kind,
                        source.name,
                        str(source.url),
                        source.external_id,
                        source.status.value,
                    ),
                )

            conn.commit()

        return source
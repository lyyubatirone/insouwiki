from insouwiki.registry.postgres_connection import get_connection


def initialize_database() -> None:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS documents (
                    permanent_id TEXT PRIMARY KEY,
                    origin_key TEXT UNIQUE NOT NULL,
                    document_kind TEXT NOT NULL,
                    title TEXT NOT NULL,
                    author TEXT,
                    original_url TEXT NOT NULL,
                    discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
            )

        conn.commit()
from insouwiki.registry.postgres_connection import get_connection


def initialize_database() -> None:
    with get_connection() as conn:
        with conn.cursor() as cur:

            #
            # Sources documentaires
            #
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS sources (
                    permanent_id TEXT PRIMARY KEY,
                    source_kind TEXT NOT NULL,
                    name TEXT NOT NULL,
                    status TEXT NOT NULL,
                    metadata JSONB NOT NULL DEFAULT '{}',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP
                );
                """
            )

            #
            # Canaux officiels de diffusion d'une source
            #
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS source_endpoints (
                    permanent_id TEXT PRIMARY KEY,
                    source_permanent_id TEXT NOT NULL REFERENCES sources(permanent_id),

                    platform TEXT NOT NULL,
                    url TEXT UNIQUE NOT NULL,
                    canonical_url TEXT UNIQUE NOT NULL,
                    external_id TEXT,
                    status TEXT NOT NULL,

                    metadata JSONB NOT NULL DEFAULT '{}',
                    first_discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_synchronized_at TIMESTAMP
                );
                """
            )

            #
            # Documents publiés par une source
            #
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS documents (
                    permanent_id TEXT PRIMARY KEY,

                    source_permanent_id TEXT REFERENCES sources(permanent_id),
                    discovered_from_endpoint_permanent_id TEXT REFERENCES source_endpoints(permanent_id),

                    origin_key TEXT UNIQUE NOT NULL,
                    document_kind TEXT NOT NULL,
                    title TEXT NOT NULL,
                    author TEXT,
                    original_url TEXT NOT NULL,

                    source_platform TEXT,
                    external_id TEXT,
                    published_at TIMESTAMP,
                    thumbnail_url TEXT,
                    documentary_nature TEXT,
                    status TEXT,

                    discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    metadata JSONB NOT NULL DEFAULT '{}'
                );
                """
            )

            cur.execute(
                """
                ALTER TABLE documents
                ADD COLUMN IF NOT EXISTS source_platform TEXT;
                """
            )

            cur.execute(
                """
                ALTER TABLE documents
                ADD COLUMN IF NOT EXISTS external_id TEXT;
                """
            )

            cur.execute(
                """
                ALTER TABLE documents
                ADD COLUMN IF NOT EXISTS published_at TIMESTAMP;
                """
            )

            cur.execute(
                """
                ALTER TABLE documents
                ADD COLUMN IF NOT EXISTS thumbnail_url TEXT;
                """
            )

            cur.execute(
                """
                ALTER TABLE documents
                ADD COLUMN IF NOT EXISTS documentary_nature TEXT;
                """
            )

            cur.execute(
                """
                ALTER TABLE documents
                ADD COLUMN IF NOT EXISTS status TEXT;
                """
            )

            #
            # Séquences documentaires
            #
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS documentary_sequences (
                    permanent_id TEXT PRIMARY KEY,

                    document_id TEXT NOT NULL REFERENCES documents(permanent_id),

                    start_seconds INTEGER NOT NULL,
                    end_seconds INTEGER NOT NULL,

                    text TEXT NOT NULL
                );
                """
            )

        conn.commit()
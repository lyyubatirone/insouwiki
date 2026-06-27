from __future__ import annotations

import json

from insouwiki.core.source import Source
from insouwiki.core.source import SourceKind
from insouwiki.registry.postgres_connection import get_connection


class SourceRepository:
    """Repository PostgreSQL des sources documentaires."""

    def create(self, source: Source) -> Source:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO sources (
                        permanent_id,
                        source_kind,
                        name,
                        status,
                        metadata
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        source.permanent_id,
                        source.kind.value,
                        source.name,
                        source.status,
                        json.dumps(source.metadata),
                    ),
                )

            conn.commit()

        return source

    def get(self, permanent_id: str) -> Source | None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT permanent_id, source_kind, name, status, metadata
                    FROM sources
                    WHERE permanent_id = %s
                    """,
                    (permanent_id,),
                )

                row = cur.fetchone()

        if row is None:
            return None

        return self._row_to_source(row)

    def get_by_name(self, name: str) -> Source | None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT permanent_id, source_kind, name, status, metadata
                    FROM sources
                    WHERE name = %s
                    """,
                    (name,),
                )

                row = cur.fetchone()

        if row is None:
            return None

        return self._row_to_source(row)

    def list_all(self) -> list[Source]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT permanent_id, source_kind, name, status, metadata
                    FROM sources
                    ORDER BY name
                    """
                )

                rows = cur.fetchall()

        return [self._row_to_source(row) for row in rows]

    def _row_to_source(self, row) -> Source:
        return Source(
            permanent_id=row[0],
            kind=SourceKind(row[1]),
            name=row[2],
            status=row[3],
            metadata=row[4] or {},
        )

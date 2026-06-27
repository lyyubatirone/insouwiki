from __future__ import annotations

import json

from insouwiki.domain.source_endpoint import Platform
from insouwiki.domain.source_endpoint import SourceEndpoint
from insouwiki.registry.postgres_connection import get_connection


class SourceEndpointRepository:
    """Repository PostgreSQL des canaux officiels de diffusion."""

    def create(self, endpoint: SourceEndpoint) -> SourceEndpoint:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO source_endpoints (
                        permanent_id,
                        source_permanent_id,
                        platform,
                        url,
                        canonical_url,
                        external_id,
                        status,
                        metadata
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        endpoint.permanent_id,
                        endpoint.source_permanent_id,
                        endpoint.platform.value,
                        endpoint.url,
                        endpoint.canonical_url,
                        endpoint.external_id,
                        endpoint.status,
                        json.dumps(endpoint.metadata),
                    ),
                )

            conn.commit()

        return endpoint

    def get(self, permanent_id: str) -> SourceEndpoint | None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        source_permanent_id,
                        platform,
                        url,
                        canonical_url,
                        external_id,
                        status,
                        metadata
                    FROM source_endpoints
                    WHERE permanent_id = %s
                    """,
                    (permanent_id,),
                )

                row = cur.fetchone()

        if row is None:
            return None

        return self._row_to_endpoint(row)

    def get_by_url(self, url: str) -> SourceEndpoint | None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        source_permanent_id,
                        platform,
                        url,
                        canonical_url,
                        external_id,
                        status,
                        metadata
                    FROM source_endpoints
                    WHERE url = %s
                    """,
                    (url,),
                )

                row = cur.fetchone()

        if row is None:
            return None

        return self._row_to_endpoint(row)

    def list_for_source(self, source_permanent_id: str) -> list[SourceEndpoint]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        source_permanent_id,
                        platform,
                        url,
                        canonical_url,
                        external_id,
                        status,
                        metadata
                    FROM source_endpoints
                    WHERE source_permanent_id = %s
                    ORDER BY platform, url
                    """,
                    (source_permanent_id,),
                )

                rows = cur.fetchall()

        return [self._row_to_endpoint(row) for row in rows]

    def _row_to_endpoint(self, row) -> SourceEndpoint:
        return SourceEndpoint(
            permanent_id=row[0],
            source_permanent_id=row[1],
            platform=Platform(row[2]),
            url=row[3],
            canonical_url=row[4],
            external_id=row[5],
            status=row[6],
            metadata=row[7] or {},
        )
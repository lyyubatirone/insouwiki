from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)
from insouwiki.domain.documentary_period_repository import (
    DocumentaryPeriodRepository,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
)


class PostgresDocumentaryPeriodRepository(
    DocumentaryPeriodRepository,
):
    """
    Référentiel PostgreSQL des périodes documentaires.
    """

    def list_all(
        self,
    ) -> tuple[DocumentaryPeriod, ...]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        label,
                        starts_at,
                        ends_at,
                        definition
                    FROM documentary_periods
                    ORDER BY starts_at, label
                    """
                )

                rows = cur.fetchall()

        return tuple(
            self._build_period(row)
            for row in rows
        )

    def register(
        self,
        period: DocumentaryPeriod,
    ) -> DocumentaryPeriod:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if period.permanent_id is None:
                    cur.execute(
                        """
                        SELECT permanent_id
                        FROM documentary_periods
                        WHERE permanent_id ~ '^PRD-[0-9]{8}$'
                        ORDER BY permanent_id DESC
                        LIMIT 1
                        """
            )

                    row = cur.fetchone()

                    if row is None:
                        next_id = 1
                    else:
                        next_id = int(
                            row[0].removeprefix("PRD-")
                        ) + 1

                    period = DocumentaryPeriod(
                        permanent_id=f"PRD-{next_id:08d}",
                        label=period.label,
                        starts_at=period.starts_at,
                        ends_at=period.ends_at,
                        definition=period.definition,
                    )

                cur.execute(
                    """
                    INSERT INTO documentary_periods (
                        permanent_id,
                        label,
                        starts_at,
                        ends_at,
                        definition
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        period.permanent_id,
                        period.label,
                        period.starts_at,
                        period.ends_at,
                        period.definition,
                    ),
                )

            conn.commit()

        return period

    def _build_period(
        self,
        row,
    ) -> DocumentaryPeriod:
        return DocumentaryPeriod(
            permanent_id=row[0],
            label=row[1],
            starts_at=row[2],
            ends_at=row[3],
            definition=row[4],
        )

    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> DocumentaryPeriod | None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        label,
                        starts_at,
                        ends_at,
                        definition
                    FROM documentary_periods
                    WHERE permanent_id = %s
                    """,
                    (permanent_id,),
                )

                row = cur.fetchone()

        if row is None:
            return None

        return self._build_period(row)
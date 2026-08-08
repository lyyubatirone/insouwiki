from datetime import date

from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)
from insouwiki.registry.postgres_documentary_period_repository import (
    PostgresDocumentaryPeriodRepository,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
)


def test_postgres_documentary_period_repository_registers_and_lists_periods():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documentary_periods
                WHERE permanent_id = %s
                """,
                ("PRD-TEST-000002",),
            )

        conn.commit()

    repository = PostgresDocumentaryPeriodRepository()

    period = DocumentaryPeriod(
        permanent_id="PRD-TEST-000002",
        label="Période documentaire de test",
        starts_at=date(2022, 1, 1),
        ends_at=date(2022, 12, 31),
        definition=(
            "Période créée pour tester le référentiel PostgreSQL."
        ),
    )

    repository.register(period)

    periods = repository.list_all()

    assert period in periods

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documentary_periods
                WHERE permanent_id = %s
                """,
                (period.permanent_id,),
            )

        conn.commit()

def test_postgres_documentary_period_repository_assigns_permanent_id():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documentary_periods
                WHERE label = %s
                """,
                ("Période automatique de test",),
            )

        conn.commit()

    repository = PostgresDocumentaryPeriodRepository()

    period = DocumentaryPeriod(
        label="Période automatique de test",
        starts_at=date(2024, 1, 1),
        ends_at=date(2024, 12, 31),
        definition=(
            "Période créée pour tester "
            "l'attribution automatique d'un identifiant."
        ),
    )

    registered = repository.register(period)

    assert registered.permanent_id is not None
    assert registered.permanent_id.startswith("PRD-")

def test_postgres_documentary_period_repository_gets_period_by_permanent_id():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documentary_periods
                WHERE permanent_id = %s
                """,
                ("PRD-TEST-GET-000001",),
            )

        conn.commit()

    repository = PostgresDocumentaryPeriodRepository()

    period = DocumentaryPeriod(
        permanent_id="PRD-TEST-GET-000001",
        label="Période documentaire de lecture",
        starts_at=date(2021, 1, 1),
        ends_at=date(2021, 12, 31),
        definition=(
            "Période créée pour tester "
            "get_by_permanent_id."
        ),
    )

    repository.register(period)

    result = repository.get_by_permanent_id(
        "PRD-TEST-GET-000001",
    )

    assert result == period

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documentary_periods
                WHERE permanent_id = %s
                """,
                (period.permanent_id,),
            )

        conn.commit()
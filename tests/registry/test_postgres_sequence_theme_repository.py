from insouwiki.domain.sequence_theme_association import (
    SequenceThemeAssociation,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
)
from insouwiki.registry.postgres_sequence_theme_repository import (
    PostgresSequenceThemeRepository,
)


def test_postgres_sequence_theme_repository_registers_and_finds_associations():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM sequence_theme_associations
                WHERE sequence_id = %s
                AND theme_id = %s
                """,
                (
                    "SEQ-00000001",
                    "THM-00000001",
                ),
            )

        conn.commit()

    repository = PostgresSequenceThemeRepository()

    association = SequenceThemeAssociation(
        sequence_id="SEQ-00000001",
        theme_id="THM-00000001",
    )

    repository.register(
        association,
    )

    by_sequence = repository.find_by_sequence(
        "SEQ-00000001",
    )

    by_theme = repository.find_by_theme(
        "THM-00000001",
    )

    assert association in by_sequence
    assert association in by_theme

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM sequence_theme_associations
                WHERE sequence_id = %s
                AND theme_id = %s
                """,
                (
                    association.sequence_id,
                    association.theme_id,
                ),
            )

        conn.commit()
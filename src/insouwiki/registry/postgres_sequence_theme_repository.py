from insouwiki.domain.sequence_theme_association import (
    SequenceThemeAssociation,
)
from insouwiki.domain.sequence_theme_repository import (
    SequenceThemeRepository,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
)


class PostgresSequenceThemeRepository(
    SequenceThemeRepository,
):
    """
    Référentiel PostgreSQL des associations
    entre séquences et thèmes.
    """

    def register(
        self,
        association: SequenceThemeAssociation,
    ) -> SequenceThemeAssociation:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO sequence_theme_associations (
                        sequence_id,
                        theme_id
                    )
                    VALUES (%s, %s)
                    """,
                    (
                        association.sequence_id,
                        association.theme_id,
                    ),
                )

            conn.commit()

        return association

    def find_by_sequence(
        self,
        sequence_id: str,
    ) -> tuple[SequenceThemeAssociation, ...]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        sequence_id,
                        theme_id
                    FROM sequence_theme_associations
                    WHERE sequence_id = %s
                    ORDER BY theme_id
                    """,
                    (sequence_id,),
                )

                rows = cur.fetchall()

        return tuple(
            SequenceThemeAssociation(
                sequence_id=row[0],
                theme_id=row[1],
            )
            for row in rows
        )

    def find_by_theme(
        self,
        theme_id: str,
    ) -> tuple[SequenceThemeAssociation, ...]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        sequence_id,
                        theme_id
                    FROM sequence_theme_associations
                    WHERE theme_id = %s
                    ORDER BY sequence_id
                    """,
                    (theme_id,),
                )

                rows = cur.fetchall()

        return tuple(
            SequenceThemeAssociation(
                sequence_id=row[0],
                theme_id=row[1],
            )
            for row in rows
        )
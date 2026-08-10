from insouwiki.domain.documentary_theme import (
    DocumentaryTheme,
)
from insouwiki.domain.documentary_theme_repository import (
    DocumentaryThemeRepository,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
)


class PostgresDocumentaryThemeRepository(
    DocumentaryThemeRepository,
):
    """
    Référentiel PostgreSQL des thèmes documentaires.
    """

    def list_all(
        self,
    ) -> tuple[DocumentaryTheme, ...]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        label,
                        definition
                    FROM documentary_themes
                    ORDER BY label
                    """
                )

                rows = cur.fetchall()

        return tuple(
            self._build_theme(row)
            for row in rows
        )

    def register(
        self,
        theme: DocumentaryTheme,
    ) -> DocumentaryTheme:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if theme.permanent_id is None:
                    cur.execute(
                        """
                        SELECT permanent_id
                        FROM documentary_themes
                        WHERE permanent_id ~ '^THM-[0-9]{8}$'
                        ORDER BY permanent_id DESC
                        LIMIT 1
                        """
                    )

                    row = cur.fetchone()

                    if row is None:
                        next_id = 1
                    else:
                        next_id = int(
                            row[0].removeprefix("THM-")
                        ) + 1

                    theme = DocumentaryTheme(
                        permanent_id=f"THM-{next_id:08d}",
                        label=theme.label,
                        definition=theme.definition,
                    )

                cur.execute(
                    """
                    INSERT INTO documentary_themes (
                        permanent_id,
                        label,
                        definition
                    )
                    VALUES (%s, %s, %s)
                    """,
                    (
                        theme.permanent_id,
                        theme.label,
                        theme.definition,
                    ),
                )

            conn.commit()

        return theme

    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> DocumentaryTheme | None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        permanent_id,
                        label,
                        definition
                    FROM documentary_themes
                    WHERE permanent_id = %s
                    """,
                    (permanent_id,),
                )

                row = cur.fetchone()

        if row is None:
            return None

        return self._build_theme(row)

    def _build_theme(
        self,
        row,
    ) -> DocumentaryTheme:
        return DocumentaryTheme(
            permanent_id=row[0],
            label=row[1],
            definition=row[2],
        )
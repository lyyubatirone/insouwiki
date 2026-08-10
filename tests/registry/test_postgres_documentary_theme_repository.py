from insouwiki.domain.documentary_theme import (
    DocumentaryTheme,
)
from insouwiki.registry.postgres_connection import (
    get_connection,
)
from insouwiki.registry.postgres_documentary_theme_repository import (
    PostgresDocumentaryThemeRepository,
)


def test_postgres_documentary_theme_repository_registers_and_lists_themes():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documentary_themes
                WHERE permanent_id = %s
                """,
                ("THM-TEST-000001",),
            )

        conn.commit()

    repository = PostgresDocumentaryThemeRepository()

    theme = DocumentaryTheme(
        permanent_id="THM-TEST-000001",
        label="Retraites",
        definition=(
            "Thème créé pour tester "
            "le référentiel PostgreSQL."
        ),
    )

    repository.register(theme)

    themes = repository.list_all()

    assert theme in themes

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documentary_themes
                WHERE permanent_id = %s
                """,
                (theme.permanent_id,),
            )

        conn.commit()

def test_postgres_documentary_theme_repository_assigns_permanent_id():
    repository = PostgresDocumentaryThemeRepository()

    theme = DocumentaryTheme(
        label="Thème automatique de test",
        definition=(
            "Thème créé pour tester "
            "l'attribution automatique d'un identifiant."
        ),
    )

    registered = repository.register(theme)

    assert registered.permanent_id is not None
    assert registered.permanent_id.startswith("THM-")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM documentary_themes
                WHERE permanent_id = %s
                """,
                (registered.permanent_id,),
            )

        conn.commit()
from insouwiki.domain.documentary_theme import (
    DocumentaryTheme,
)
from insouwiki.registry.postgres_documentary_theme_repository import (
    PostgresDocumentaryThemeRepository,
)


def main() -> None:
    repository = PostgresDocumentaryThemeRepository()

    theme = DocumentaryTheme(
        permanent_id="THM-00000001",
        label="Retraites",
        definition=(
            "Prises de parole relatives aux systèmes "
            "de retraite, à leur financement, à l'âge "
            "de départ et aux droits à pension."
        ),
    )

    existing = repository.get_by_permanent_id(
        theme.permanent_id,
    )

    if existing is None:
        registered = repository.register(theme)

        print(
            f"{registered.permanent_id} — "
            f"{registered.label}"
        )
    else:
        print(
            f"{existing.permanent_id} — "
            f"{existing.label} existe déjà"
        )


if __name__ == "__main__":
    main()
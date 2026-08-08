from datetime import date

from insouwiki.domain.documentary_period import (
    DocumentaryPeriod,
)
from insouwiki.registry.postgres_documentary_period_repository import (
    PostgresDocumentaryPeriodRepository,
)


def main() -> None:
    repository = PostgresDocumentaryPeriodRepository()

    period = DocumentaryPeriod(
        permanent_id="PRD-00000001",
        label="Campagne présidentielle 2022",
        starts_at=date(2020, 1, 16),
        ends_at=date(2022, 4, 24),
        definition=(
            "La période débute à la date de la première "
            "déclaration publique de candidature à "
            "l'élection présidentielle de 2022."
        ),
    )

    existing = repository.get_by_permanent_id(
        period.permanent_id,
    )

    if existing is None:
        registered = repository.register(period)

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
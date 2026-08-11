from decimal import Decimal

from insouwiki.registry.postgres import (
    PostgresDocumentRepository,
)
from insouwiki.services.documentary_processing_batch_preparer import (
    DocumentaryProcessingBatchPreparer,
)
from insouwiki.services.documentary_processing_cost_estimator import (
    DocumentaryProcessingCostEstimator,
)


def main() -> None:
    repository = PostgresDocumentRepository()

    preparer = DocumentaryProcessingBatchPreparer(
        repository=repository,
    )

    batch = preparer.prepare(
        name="Lot de démonstration",
        document_ids=[
            "SRC-00000836",
            "SRC-00000045",
            "SRC-00000816",
        ],
    )

    estimator = DocumentaryProcessingCostEstimator(
        price_per_minute=Decimal("0.0045"),
    )

    estimated_cost = estimator.estimate(
        batch,
    )

    total_seconds = int(
        batch.total_duration.total_seconds()
    )

    hours, remainder = divmod(
        total_seconds,
        3600,
    )

    minutes, seconds = divmod(
        remainder,
        60,
    )

    print(f"Lot : {batch.name}")
    print(
        f"Documents : {batch.document_count}"
    )
    print(
        "Durée totale : "
        f"{hours} h {minutes:02d} min "
        f"{seconds:02d} s"
    )
    print(
        "Coût estimé : "
        f"{estimated_cost:.2f} $"
    )
    print(
        f"Statut : {batch.status}"
    )


if __name__ == "__main__":
    main()
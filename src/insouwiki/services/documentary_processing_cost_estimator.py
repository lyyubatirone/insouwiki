from decimal import Decimal

from insouwiki.domain.documentary_processing_batch import (
    DocumentaryProcessingBatch,
)


class DocumentaryProcessingCostEstimator:
    def __init__(
        self,
        price_per_minute: Decimal,
    ) -> None:
        self.price_per_minute = price_per_minute

    def estimate(
        self,
        batch: DocumentaryProcessingBatch,
    ) -> Decimal:
        total_minutes = (
            Decimal(
                str(
                    batch.total_duration.total_seconds()
                )
            )
            / Decimal("60")
        )

        return (
            total_minutes
            * self.price_per_minute
        )

    
from datetime import timedelta
from decimal import Decimal

from insouwiki.domain.documentary_processing_batch import (
    DocumentaryProcessingBatch,
)
from insouwiki.services.documentary_processing_cost_estimator import (
    DocumentaryProcessingCostEstimator,
)


def test_estimates_processing_cost_from_duration_and_minute_rate():
    batch = DocumentaryProcessingBatch(
        name="Retraites",
        document_ids=[
            "SRC-00000001",
            "SRC-00000002",
        ],
        document_durations=[
            timedelta(hours=1),
            timedelta(
                hours=1,
                minutes=15,
            ),
        ],
    )

    estimator = DocumentaryProcessingCostEstimator(
        price_per_minute=Decimal("0.0045"),
    )

    cost = estimator.estimate(
        batch,
    )

    assert cost == Decimal("0.6075")

def test_estimates_cost_for_large_processing_batch():
    batch = DocumentaryProcessingBatch(
        name="Lot de 10 dollars",
        document_ids=[
            "SRC-00000001",
        ],
        document_durations=[
            timedelta(hours=37),
        ],
    )

    estimator = DocumentaryProcessingCostEstimator(
        price_per_minute=Decimal("0.0045"),
    )

    cost = estimator.estimate(
        batch,
    )

    assert cost == Decimal("9.9900")
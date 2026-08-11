from dataclasses import dataclass, field, replace
from datetime import timedelta


@dataclass(frozen=True)
class DocumentaryProcessingBatch:
    permanent_id: str | None = None
    name: str = ""
    document_ids: list[str] = field(
        default_factory=list,
    )
    document_durations: list[timedelta] = field(
        default_factory=list,
    )
    status: str = "prepared"

    @property
    def document_count(self) -> int:
        return len(self.document_ids)

    @property
    def total_duration(self) -> timedelta:
        return sum(
            self.document_durations,
            start=timedelta(),
        )

    def approve(
        self,
    ) -> "DocumentaryProcessingBatch":
        return replace(
            self,
            status="approved",
        )

    def mark_processed(
        self,
    ) -> "DocumentaryProcessingBatch":
        if self.status != "approved":
            raise ValueError(
                "Only an approved batch "
                "can be marked as processed."
            )

        return replace(
            self,
            status="processed",
        )
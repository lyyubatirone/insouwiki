from dataclasses import dataclass
from dataclasses import dataclass, field

from insouwiki.domain.document import Document


@dataclass(frozen=True)
class DocumentaryInventory:
    from dataclasses import dataclass, field

@dataclass(frozen=True)
class DocumentaryInventory:
    documents: tuple[Document, ...] = field(default_factory=tuple)

    @property
    def document_count(self) -> int:
        return len(self.documents)
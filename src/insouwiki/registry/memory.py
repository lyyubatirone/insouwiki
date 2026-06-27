from insouwiki.domain.models import Document
from insouwiki.registry.repository import DocumentRepository
from insouwiki.registry.result import RegistrationResult


class MemoryDocumentRepository(DocumentRepository):

    def __init__(self):
        self.documents: dict[str, Document] = {}
        self.next_id = 1

    def exists(self, origin_key: str) -> bool:
        return origin_key in self.documents

    def count(self) -> int:
        return len(self.documents)

    def register(self, document: Document) -> RegistrationResult:

        if self.exists(document.origin_key):
            existing = self.documents[document.origin_key]

            return RegistrationResult(
                document_id=existing.permanent_id,
                created=False,
            )

        document.permanent_id = f"SRC-{self.next_id:08d}"
        self.next_id += 1

        self.documents[document.origin_key] = document

        return RegistrationResult(
            document_id=document.permanent_id,
            created=True,
        )
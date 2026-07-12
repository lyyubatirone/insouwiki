from insouwiki.domain.document import Document
from insouwiki.domain.enums import ProcessingStatus
from insouwiki.registry.repository import DocumentRepository
from insouwiki.registry.result import RegistrationResult


class MemoryDocumentRepository(DocumentRepository):

    def __init__(self) -> None:
        self._documents: dict[str, Document] = {}
        self._next_id = 1

    def exists(self, origin_key: str) -> bool:
        return origin_key in self._documents

    def count(self) -> int:
        return len(self._documents)

    def register(
        self,
        document: Document,
    ) -> RegistrationResult:
        return self.register_many([document])[0]

    def register_many(
        self,
        documents: list[Document],
    ) -> list[RegistrationResult]:
        results: list[RegistrationResult] = []

        for document in documents:
            if self.exists(document.origin_key):
                existing = self._documents[
                    document.origin_key
                ]

                document.permanent_id = (
                    existing.permanent_id
                )

                results.append(
                    RegistrationResult(
                        document_id=existing.permanent_id,
                        created=False,
                    )
                )
                continue

            document.permanent_id = (
                f"SRC-{self._next_id:08d}"
            )
            self._next_id += 1

            self._documents[
                document.origin_key
            ] = document

            results.append(
                RegistrationResult(
                    document_id=document.permanent_id,
                    created=True,
                )
            )

        return results

    def find_all(self) -> list[Document]:
        return list(self._documents.values())

    def get_by_permanent_id(
        self,
        permanent_id: str,
    ) -> Document | None:
        for document in self._documents.values():
            if document.permanent_id == permanent_id:
                return document

        return None

    def get_by_original_url(
        self,
        original_url: str,
    ) -> Document | None:
        for document in self._documents.values():
            if document.original_url == original_url:
                return document

        return None

    def update_status(
        self,
        origin_key: str,
        status: ProcessingStatus,
    ) -> None:
        self._documents[
            origin_key
        ].status = status
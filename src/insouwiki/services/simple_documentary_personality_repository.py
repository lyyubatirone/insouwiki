import re
import unicodedata

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_personality import (
    DocumentaryPersonality,
)
from insouwiki.domain.documentary_personality_repository import (
    DocumentaryPersonalityRepository,
)


class SimpleDocumentaryPersonalityRepository(
    DocumentaryPersonalityRepository,
):
    def __init__(
        self,
        documents: list[Document] | None = None,
    ):
        self.documents = documents or []

    def list_all(
        self,
    ) -> list[DocumentaryPersonality]:
        document_counts: dict[str, int] = {}

        for document in self.documents:
            if not document.author:
                continue

            author = document.author.strip()

            if not author:
                continue

            document_counts[author] = (
                document_counts.get(author, 0) + 1
            )

        authors = sorted(document_counts)

        return [
            DocumentaryPersonality(
                permanent_id=f"PER-{index:08d}",
                slug=self._slugify(author),
                display_name=author,
                document_count=document_counts[author],
            )
            for index, author in enumerate(
                authors,
                start=1,
            )
        ]

    @staticmethod
    def _slugify(value: str) -> str:
        normalized = unicodedata.normalize(
            "NFKD",
            value,
        )

        ascii_value = normalized.encode(
            "ascii",
            "ignore",
        ).decode("ascii")

        return re.sub(
            r"[^a-z0-9]+",
            "-",
            ascii_value.lower(),
        ).strip("-")
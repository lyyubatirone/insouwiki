from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from insouwiki.domain.document import Document
from insouwiki.domain.documentary_sequence import DocumentarySequence
from insouwiki.services.timestamp_link_builder import TimestampLinkBuilder


class YouTubeTimestampLinkBuilder(TimestampLinkBuilder):
    """
    Construit un lien YouTube horodaté
    à partir d'un document et d'une séquence documentaire.
    """

    def build(
        self,
        document: Document,
        sequence: DocumentarySequence,
    ) -> str:
        parsed_url = urlparse(str(document.original_url))
        query_parameters = parse_qs(parsed_url.query)

        query_parameters["t"] = [
            f"{int(sequence.start.total_seconds())}s"
        ]

        updated_query = urlencode(query_parameters, doseq=True)

        return urlunparse(
            parsed_url._replace(query=updated_query)
        )
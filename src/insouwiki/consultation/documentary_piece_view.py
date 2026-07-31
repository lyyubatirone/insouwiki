from pydantic import BaseModel


class DocumentaryPieceView(BaseModel):
    """
    Vue de consultation d'une pièce documentaire.
    """

    author: str
    document_title: str
    sequence_text: str
    sequence_start: str
    sequence_end: str
    document_url: str
    
    @property
    def start_seconds(self) -> int:
        hours, minutes, seconds = (
            int(part)
            for part in self.sequence_start.split(":")
        )

        return (
            hours * 3600
            + minutes * 60
            + seconds
        )

    @property
    def youtube_url(self) -> str:
        separator = "&" if "?" in self.document_url else "?"

        return (
            f"{self.document_url}"
            f"{separator}t={self.start_seconds}s"
        )

    @property
    def embed_url(self) -> str:
        video_id = self.document_url.split("v=")[-1].split("&")[0]

        return (
            f"https://www.youtube.com/embed/{video_id}"
            f"?start={self.start_seconds}"
        )

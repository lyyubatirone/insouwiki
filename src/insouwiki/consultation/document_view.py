from pydantic import BaseModel


class DocumentView(BaseModel):
    """
    Vue de consultation d'un document.
    """

    title: str

    author: str | None = None

    original_url: str

    permanent_id: str
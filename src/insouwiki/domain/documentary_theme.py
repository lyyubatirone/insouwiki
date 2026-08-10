from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentaryTheme:
    """
    Thème documentaire appartenant au référentiel InsouWiki.
    """

    label: str
    permanent_id: str | None = None
    definition: str | None = None
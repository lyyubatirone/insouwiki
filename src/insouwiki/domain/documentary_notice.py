from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentaryNotice:
    """
    Présente un document avant sa consultation.
    """

    documentary_contexts: tuple[str, ...] = ()
    themes: tuple[str, ...] = ()
from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentaryQuestion:
    """
    Question documentaire formulée librement par le lecteur.

    Le texte original est conservé sans transformation.
    """

    text: str
"""
Un indicateur documentaire ne décrit pas le document.

Il décrit une connaissance documentaire utilisée
pour interpréter les observations d'un document.
"""

from pydantic import BaseModel


class DocumentaryIndicator(BaseModel):
    """
    Connaissance documentaire permettant d'interpréter
    une ou plusieurs observations.
    """

    name: str
    description: str
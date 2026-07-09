from pydantic import BaseModel


class DocumentaryAnalysis(BaseModel):
    """
    Raisonnement documentaire explicable.

    Une analyse documentaire ne constitue pas une décision.
    Elle expose les observations, les indicateurs mobilisés,
    l'explication et la conclusion proposée.
    """

    observations: list[str]
    indicators: list[str]
    explanation: str
    proposed_conclusion: str
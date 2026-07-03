from pydantic import BaseModel


class VerificationRequest(BaseModel):
    """
    Demande de vérification documentaire.

    Représente la demande formulée par un lecteur
    souhaitant ouvrir un dossier documentaire afin
    de vérifier une affirmation ou d'explorer un sujet
    à partir des sources primaires.
    """

    query: str
from pydantic import BaseModel

from insouwiki.domain.documentary_piece import DocumentaryPiece


class DocumentaryDossier(BaseModel):
    """
    Dossier documentaire.

    Un dossier documentaire rassemble des pièces documentaires
    permettant au lecteur de vérifier une affirmation à partir
    des sources primaires.

    Il constitue le principal objet remis au lecteur par le
    moteur de vérification documentaire.
    """

    title: str

    pieces: list[DocumentaryPiece]
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

    @property
    def piece_count(self) -> int:
        """
        Nombre de pièces documentaires contenues dans le dossier.
        """
        return len(self.pieces)

    @property
    def document_count(self) -> int:
        """
        Nombre de documents distincts représentés dans le dossier.
        """
        return len(
            {
                piece.document_title
                for piece in self.pieces
            }
        )
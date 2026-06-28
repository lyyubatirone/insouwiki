from abc import ABC, abstractmethod
from pathlib import Path

from insouwiki.domain.document import Document


class AudioExtractor(ABC):
    """
    Contrat des extracteurs audio.

    Un extracteur produit un fichier audio à partir
    d'un document audiovisuel.
    """

    @abstractmethod
    def extract(
        self,
        document: Document,
        output_directory: Path,
    ) -> Path:
        """
        Extrait la piste audio du document dans le dossier indiqué.

        Retourne le chemin du fichier audio créé.
        """
        ...
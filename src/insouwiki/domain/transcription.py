from datetime import UTC, datetime

from pydantic import BaseModel, Field


class Transcription(BaseModel):
    """
    Représentation textuelle d'un document audiovisuel.

    Une transcription constitue une ressource documentaire dérivée.
    Elle ne remplace jamais le document d'origine et lui reste
    systématiquement rattachée.
    """

    permanent_id: str | None = Field(
        default=None,
        description="Identifiant documentaire permanent de la transcription.",
    )

    document_id: str = Field(
        description="Identifiant permanent du document auquel appartient cette transcription.",
    )

    language: str = Field(
        description="Langue de la transcription (ISO 639-1 recommandé).",
    )

    text: str = Field(
        description="Texte intégral de la transcription.",
    )

    engine: str = Field(
        description="Moteur ou méthode ayant produit la transcription.",
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Date de création de la transcription.",
    )
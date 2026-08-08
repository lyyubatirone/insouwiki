from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentaryContext:
    """
    Contexte historique ou institutionnel
    dans lequel un document a été produit.
    """

    label: str
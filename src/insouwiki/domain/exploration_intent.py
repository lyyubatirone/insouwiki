from enum import Enum


class ExplorationIntent(str, Enum):
    """
    Intentions fondamentales d'exploration documentaire.

    Chaque intention correspond à un scénario de référence
    de la phase d'incarnation d'InsouWiki.
    """

    UNDERSTAND = "understand"
    COMPARE = "compare"
    VERIFY = "verify"
    CONTEXT = "context"
    FOLLOW_EVOLUTION = "follow_evolution"
    DISCOVER = "discover"
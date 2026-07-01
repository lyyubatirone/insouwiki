from enum import Enum


class DocumentaryRelationType(str, Enum):
    """
    Catégories fondamentales des relations documentaires.
    """

    SAME_AUTHOR = "same_author"
    SAME_TOPIC = "same_topic"
    SAME_EVENT = "same_event"

    CHRONOLOGY = "chronology"

    COMPLEMENTS = "complements"
    REFINES = "refines"

    CONSISTENT = "consistent"
    CONTRADICTS = "contradicts"

    EVOLUTION = "evolution"
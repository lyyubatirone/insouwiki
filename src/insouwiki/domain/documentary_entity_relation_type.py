from enum import Enum


class DocumentaryEntityRelationType(str, Enum):
    """
    Types de relations documentaires entre entités.
    """

    MEMBER_OF = "MEMBER_OF"

    PART_OF = "PART_OF"

    HOLDS_POSITION = "HOLDS_POSITION"
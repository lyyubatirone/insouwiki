from enum import Enum


class DocumentaryEntityType(str, Enum):
    """
    Types d'entités documentaires.
    """

    PERSON = "PERSON"

    INSTITUTION = "INSTITUTION"

    POLITICAL_ORGANIZATION = "POLITICAL_ORGANIZATION"

    PARLIAMENTARY_GROUP = "PARLIAMENTARY_GROUP"

    PARLIAMENTARY_COMMISSION = "PARLIAMENTARY_COMMISSION"

    PLACE = "PLACE"

    EVENT = "EVENT"
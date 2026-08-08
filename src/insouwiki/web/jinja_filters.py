from datetime import date

MONTHS = (
    "",
    "janvier",
    "février",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    "août",
    "septembre",
    "octobre",
    "novembre",
    "décembre",
)


def french_date(value: date | None) -> str:
    if value is None:
        return ""

    return (
        f"{value.day} "
        f"{MONTHS[value.month]} "
        f"{value.year}"
    )
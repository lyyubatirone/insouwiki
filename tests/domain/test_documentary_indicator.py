from insouwiki.domain.documentary_indicator import (
    DocumentaryIndicator,
)


def test_documentary_indicator_describes_documentary_knowledge():
    indicator = DocumentaryIndicator(
        name="Transition explicite",
        description=(
            "Une annonce explicite de changement de sujet "
            "constitue un indice de rupture documentaire."
        ),
    )

    assert indicator.name == "Transition explicite"
    assert indicator.description == (
        "Une annonce explicite de changement de sujet "
        "constitue un indice de rupture documentaire."
    )
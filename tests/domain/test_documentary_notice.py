from insouwiki.domain.documentary_notice import (
    DocumentaryNotice,
)


def test_creates_documentary_notice():
    notice = DocumentaryNotice(
        documentary_contexts=(
            "Mandat présidentiel 2017–2022",
            "Campagne présidentielle 2022",
            "XVe législature (2017–2022)",
        ),
        topics=(
            "Retraite à 60 ans",
            "Financement des retraites",
        ),
    )

    assert notice.documentary_contexts == (
        "Mandat présidentiel 2017–2022",
        "Campagne présidentielle 2022",
        "XVe législature (2017–2022)",
    )

    assert notice.topics == (
        "Retraite à 60 ans",
        "Financement des retraites",
    )
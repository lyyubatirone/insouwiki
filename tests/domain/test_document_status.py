from insouwiki.domain.enums import ProcessingStatus


def test_processing_status_defines_unavailable():
    assert ProcessingStatus.UNAVAILABLE.value == "unavailable"
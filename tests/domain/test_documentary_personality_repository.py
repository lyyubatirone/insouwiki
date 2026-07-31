from abc import ABC

from insouwiki.domain.documentary_personality_repository import (
    DocumentaryPersonalityRepository,
)


def test_repository_is_abstract():
    assert issubclass(
        DocumentaryPersonalityRepository,
        ABC,
    )
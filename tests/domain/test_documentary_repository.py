from pytest import raises

from insouwiki.domain.documentary_repository import (
    DocumentaryRepository,
)


def test_documentary_repository_is_abstract():
    with raises(TypeError):
        DocumentaryRepository()
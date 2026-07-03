from abc import ABC

from insouwiki.services.documentary_index import DocumentaryIndex


def test_documentary_index_is_abstract_service():
    assert issubclass(DocumentaryIndex, ABC)
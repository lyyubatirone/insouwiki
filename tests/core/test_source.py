from insouwiki.core.source import Source
from insouwiki.core.source import SourceKind


def test_create_source():
    source = Source(
        id=None,
        name="Jean-Luc Mélenchon",
        kind=SourceKind.PERSON,
    )

    assert source.name == "Jean-Luc Mélenchon"
    assert source.kind is SourceKind.PERSON
    assert source.enabled is True
    assert source.metadata == {}


def test_metadata_not_shared():
    s1 = Source(
        id=None,
        name="Source 1",
        kind=SourceKind.ORGANIZATION,
    )

    s2 = Source(
        id=None,
        name="Source 2",
        kind=SourceKind.ORGANIZATION,
    )

    s1.metadata["foo"] = "bar"

    assert s2.metadata == {}
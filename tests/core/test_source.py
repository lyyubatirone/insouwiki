from insouwiki.domain.source import Source
from insouwiki.domain.source import SourceKind


def test_create_source():
    source = Source(
        permanent_id="source:person:jean-luc-melenchon",
        name="Jean-Luc Mélenchon",
        kind=SourceKind.PERSON,
    )

    assert source.permanent_id == "source:person:jean-luc-melenchon"
    assert source.name == "Jean-Luc Mélenchon"
    assert source.kind is SourceKind.PERSON
    assert source.status == "active"
    assert source.metadata == {}


def test_metadata_not_shared():
    s1 = Source(
        permanent_id="source:organization:source-1",
        name="Source 1",
        kind=SourceKind.ORGANIZATION,
    )

    s2 = Source(
        permanent_id="source:organization:source-2",
        name="Source 2",
        kind=SourceKind.ORGANIZATION,
    )

    s1.metadata["foo"] = "bar"

    assert s2.metadata == {}
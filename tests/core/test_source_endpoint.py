from insouwiki.core.source_endpoint import Platform
from insouwiki.core.source_endpoint import SourceEndpoint


def test_create_source_endpoint():
    endpoint = SourceEndpoint(
        permanent_id="endpoint:youtube:jlmelenchon",
        source_permanent_id="source:person:jean-luc-melenchon",
        platform=Platform.YOUTUBE,
        url="https://www.youtube.com/@JLMelenchon",
        canonical_url="https://www.youtube.com/@JLMelenchon",
        external_id="@JLMelenchon",
    )

    assert endpoint.permanent_id == "endpoint:youtube:jlmelenchon"
    assert endpoint.source_permanent_id == "source:person:jean-luc-melenchon"
    assert endpoint.platform is Platform.YOUTUBE
    assert endpoint.status == "active"
    assert endpoint.metadata == {}


def test_metadata_not_shared():
    endpoint_1 = SourceEndpoint(
        permanent_id="endpoint:website:source-1",
        source_permanent_id="source:organization:source-1",
        platform=Platform.WEBSITE,
        url="https://example.org",
        canonical_url="https://example.org",
    )

    endpoint_2 = SourceEndpoint(
        permanent_id="endpoint:website:source-2",
        source_permanent_id="source:organization:source-2",
        platform=Platform.WEBSITE,
        url="https://example.net",
        canonical_url="https://example.net",
    )

    endpoint_1.metadata["foo"] = "bar"

    assert endpoint_2.metadata == {}
from datetime import timedelta

from insouwiki.collector.youtube import YouTubeCollector
from insouwiki.domain.discovery_request import DiscoveryRequest
from insouwiki.domain.enums import DiscoveryTargetKind


class FakeRequest:
    def __init__(
        self,
        response,
    ):
        self.response = response

    def execute(self):
        return self.response


class FakeChannels:
    def list(self, **kwargs):
        return FakeRequest(
            {
                "items": [
                    {
                        "snippet": {
                            "title": "Jean-Luc Mélenchon",
                        },
                        "contentDetails": {
                            "relatedPlaylists": {
                                "uploads": "UPLOADS",
                            }
                        },
                    }
                ]
            }
        )


class FakePlaylistItems:
    def list(self, **kwargs):
        return FakeRequest(
            {
                "items": [
                    {
                        "snippet": {
                            "title": "Vidéo de test",
                            "publishedAt": (
                                "2022-04-08T00:00:00Z"
                            ),
                            "thumbnails": {},
                        },
                        "contentDetails": {
                            "videoId": "video-123",
                        },
                    }
                ]
            }
        )


class FakeVideos:
    def list(self, **kwargs):
        return FakeRequest(
            {
                "items": [
                    {
                        "id": "video-123",
                        "contentDetails": {
                            "duration": "PT42M15S",
                        },
                    }
                ]
            }
        )


class FakeYouTube:
    def channels(self):
        return FakeChannels()

    def playlistItems(self):
        return FakePlaylistItems()

    def videos(self):
        return FakeVideos()


def test_youtube_collector_adds_video_duration():
    collector = YouTubeCollector(
        youtube=FakeYouTube(),
    )

    request = DiscoveryRequest(
        source_kind=(
            DiscoveryTargetKind.YOUTUBE_CHANNEL
        ),
        url=(
            "https://www.youtube.com/"
            "@JLMelenchon"
        ),
    )

    report = collector.discover_channel(
        request,
    )

    assert len(
        report.discovered_documents
    ) == 1

    document = (
        report.discovered_documents[0]
    )

    assert document.duration == timedelta(
        minutes=42,
        seconds=15,
    )
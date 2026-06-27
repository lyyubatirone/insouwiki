from dataclasses import dataclass
from googleapiclient.discovery import build

from insouwiki.common.settings import settings


@dataclass
class YouTubeChannel:
    title: str
    channel_id: str
    description: str
    video_count: int
    uploads_playlist_id: str


class YouTubeCollector:
    def __init__(self):
        self.youtube = build(
            "youtube",
            "v3",
            developerKey=settings.youtube_api_key,
        )

    def get_channel_from_handle(self, handle: str) -> YouTubeChannel:
        if handle.startswith("@"):
            handle = handle[1:]

        response = (
            self.youtube.channels()
            .list(
                part="snippet,statistics,contentDetails",
                forHandle=handle,
            )
            .execute()
        )

        items = response.get("items", [])

        if not items:
            raise ValueError(f"Chaîne introuvable : @{handle}")

        item = items[0]

        return YouTubeChannel(
            title=item["snippet"]["title"],
            channel_id=item["id"],
            description=item["snippet"].get("description", ""),
            video_count=int(item["statistics"].get("videoCount", 0)),
            uploads_playlist_id=item["contentDetails"]["relatedPlaylists"]["uploads"],
        )
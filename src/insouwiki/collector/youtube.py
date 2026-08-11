import re
from datetime import datetime, timedelta

from googleapiclient.discovery import build

from insouwiki.common.settings import settings
from insouwiki.domain.discovery import DiscoveryReport
from insouwiki.domain.discovery_request import DiscoveryRequest
from insouwiki.domain.document import Document
from insouwiki.domain.enums import (
    DocumentKind,
    ProcessingStatus,
)


class YouTubeCollector:
    def __init__(self, youtube=None):
        self.youtube = (
            youtube
            if youtube is not None
            else build(
                "youtube",
                "v3",
                developerKey=settings.youtube_api_key,
            )
        )

    def discover_channel(
        self,
        request: DiscoveryRequest,
    ) -> DiscoveryReport:
        started_at = datetime.now()

        handle = (
            str(request.url)
            .rstrip("/")
            .split("/")[-1]
        )

        if handle.startswith("@"):
            handle = handle[1:]

        channel_response = (
            self.youtube.channels()
            .list(
                part="snippet,statistics,contentDetails",
                forHandle=handle,
            )
            .execute()
        )

        items = channel_response.get("items", [])

        if not items:
            finished_at = datetime.now()

            return DiscoveryReport(
                request=request,
                errors=[
                    f"Chaîne introuvable : @{handle}"
                ],
                started_at=started_at,
                finished_at=finished_at,
            )

        channel = items[0]

        uploads_playlist_id = (
            channel["contentDetails"]
            ["relatedPlaylists"]
            ["uploads"]
        )

        author = channel["snippet"]["title"]

        documents: list[Document] = []
        next_page_token = None

        while True:
            playlist_response = (
                self.youtube.playlistItems()
                .list(
                    part="snippet,contentDetails",
                    playlistId=uploads_playlist_id,
                    maxResults=50,
                    pageToken=next_page_token,
                )
                .execute()
            )

            playlist_items = (
                playlist_response.get(
                    "items",
                    [],
                )
            )

            video_ids = [
                item["contentDetails"]["videoId"]
                for item in playlist_items
            ]

            durations: dict[
                str,
                timedelta | None,
            ] = {}

            if video_ids:
                videos_response = (
                    self.youtube.videos()
                    .list(
                        part="contentDetails",
                        id=",".join(video_ids),
                    )
                    .execute()
                )

                durations = {
                    item["id"]: self._parse_duration(
                        item.get(
                            "contentDetails",
                            {},
                        ).get(
                            "duration"
                        )
                    )
                    for item
                    in videos_response.get(
                        "items",
                        [],
                    )
                }

            for item in playlist_items:
                snippet = item["snippet"]

                video_id = (
                    item["contentDetails"]
                    ["videoId"]
                )

                thumbnails = snippet.get(
                    "thumbnails",
                    {},
                )

                thumbnail_url = None

                if "high" in thumbnails:
                    thumbnail_url = (
                        thumbnails["high"]["url"]
                    )
                elif "default" in thumbnails:
                    thumbnail_url = (
                        thumbnails["default"]["url"]
                    )

                documents.append(
                    Document(
                        permanent_id=None,
                        origin_key=(
                            f"youtube:{video_id}"
                        ),
                        document_kind=(
                            DocumentKind.VIDEO
                        ),
                        title=snippet["title"],
                        original_url=(
                            "https://www.youtube.com/"
                            f"watch?v={video_id}"
                        ),
                        source_platform="youtube",
                        external_id=video_id,
                        author=author,
                        published_at=(
                            snippet.get(
                                "publishedAt"
                            )
                        ),
                        duration=(
                            durations.get(
                                video_id
                            )
                        ),
                        thumbnail_url=thumbnail_url,
                        status=(
                            ProcessingStatus.DISCOVERED
                        ),
                    )
                )

            next_page_token = (
                playlist_response.get(
                    "nextPageToken"
                )
            )

            if not next_page_token:
                break

        return DiscoveryReport(
            request=request,
            discovered_documents=documents,
            started_at=started_at,
            finished_at=datetime.now(),
        )

    def _parse_duration(
        self,
        value: str | None,
    ) -> timedelta | None:
        if not value:
            return None

        match = re.fullmatch(
            r"PT"
            r"(?:(?P<hours>\d+)H)?"
            r"(?:(?P<minutes>\d+)M)?"
            r"(?:(?P<seconds>\d+)S)?",
            value,
        )

        if match is None:
            return None

        return timedelta(
            hours=int(
                match.group("hours") or 0
            ),
            minutes=int(
                match.group("minutes") or 0
            ),
            seconds=int(
                match.group("seconds") or 0
            ),
        )
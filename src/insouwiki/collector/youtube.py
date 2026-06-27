from datetime import datetime

from googleapiclient.discovery import build

from insouwiki.common.settings import settings
from insouwiki.domain.discovery import DiscoveryReport
from insouwiki.domain.enums import DocumentKind
from insouwiki.domain.enums import ProcessingStatus
from insouwiki.domain.models import DiscoveryRequest
from insouwiki.domain.document import Document


class YouTubeCollector:
    def __init__(self):
        self.youtube = build(
            "youtube",
            "v3",
            developerKey=settings.youtube_api_key,
        )

    def discover_channel(self, request: DiscoveryRequest) -> DiscoveryReport:
        started_at = datetime.now()

        handle = str(request.url).rstrip("/").split("/")[-1]
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
                errors=[f"Chaîne introuvable : @{handle}"],
                started_at=started_at,
                finished_at=finished_at,
            )

        channel = items[0]
        uploads_playlist_id = channel["contentDetails"]["relatedPlaylists"]["uploads"]
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

            for item in playlist_response.get("items", []):
                snippet = item["snippet"]
                video_id = item["contentDetails"]["videoId"]

                thumbnails = snippet.get("thumbnails", {})
                thumbnail_url = None
                if "high" in thumbnails:
                    thumbnail_url = thumbnails["high"]["url"]
                elif "default" in thumbnails:
                    thumbnail_url = thumbnails["default"]["url"]

                documents.append(
                    Document(
                        permanent_id=None,
                        origin_key=f"youtube:{video_id}",
                        document_kind=DocumentKind.VIDEO,
                        title=snippet["title"],
                        original_url=f"https://www.youtube.com/watch?v={video_id}",
                        source_platform="youtube",
                        external_id=video_id,
                        author=author,
                        published_at=snippet.get("publishedAt"),
                        thumbnail_url=thumbnail_url,
                        status=ProcessingStatus.DISCOVERED,
                    )
                )

            next_page_token = playlist_response.get("nextPageToken")
            if not next_page_token:
                break

        return DiscoveryReport(
            request=request,
            discovered_documents=documents,
            started_at=started_at,
            finished_at=datetime.now(),
        )
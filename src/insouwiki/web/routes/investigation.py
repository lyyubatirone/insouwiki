from datetime import timedelta
from urllib.parse import parse_qs, urlencode, urlparse

from fastapi import APIRouter, Query, Request
from fastapi.templating import Jinja2Templates

from insouwiki.web.services.investigation_service import (
    InvestigationService,
)

router = APIRouter()

templates = Jinja2Templates(
    directory="src/insouwiki/web/templates",
)

def build_youtube_embed_url(
    source_url: str | None,
    sequence_start: timedelta | None,
) -> str | None:
    if source_url is None:
        return None

    if sequence_start is None:
        return None

    parsed_url = urlparse(source_url)

    if parsed_url.netloc in {
        "www.youtube.com",
        "youtube.com",
        "m.youtube.com",
    }:
        video_id = parse_qs(
            parsed_url.query,
        ).get(
            "v",
            [None],
        )[0]

    elif parsed_url.netloc == "youtu.be":
        video_id = parsed_url.path.lstrip("/")

    else:
        return None

    if not video_id:
        return None

    start_seconds = int(
        sequence_start.total_seconds(),
    )

    return (
        f"https://www.youtube.com/embed/{video_id}"
        f"?start={start_seconds}"
    )

@router.get("/enquetes")
def investigation(
    request: Request,
    q: str = "",
    personality: list[str] = Query(default=[]),
):
    service = InvestigationService()

    state, clues = service.start(
        question=q,
        personalities=personality,
    )

    youtube_embed_urls = [
        build_youtube_embed_url(
            clue.source_url,
            clue.sequence_start,
        )
        for clue in clues
    ]

    personalities = service.list_personalities()

    remove_personality_urls = {}

    for current_personality in state.personalities:
        remaining_personalities = [
            personality
            for personality in state.personalities
            if personality != current_personality
        ]

        parameters = [
            ("q", state.question),
            *[
                ("personality", personality)
                for personality in remaining_personalities
            ],
        ]

        remove_personality_urls[current_personality] = (
            f"/enquetes?{urlencode(parameters)}"
        )

    return templates.TemplateResponse(
        request=request,
        name="investigation.html",
        context={
            "investigation": state,
            "clues": clues,
            "youtube_embed_urls": youtube_embed_urls,
            "personalities": personalities,
            "remove_personality_urls": (
                remove_personality_urls
            ),
        },
    )
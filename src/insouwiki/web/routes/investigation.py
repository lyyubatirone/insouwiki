from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from insouwiki.web.services.investigation_service import (
    InvestigationService,
)

from fastapi import APIRouter, Query, Request

from urllib.parse import urlencode

router = APIRouter()

templates = Jinja2Templates(
    directory="src/insouwiki/web/templates",
)


@router.get("/enquetes")
def investigation(
    request: Request,
    q: str = "",
    personality: list[str] = Query(default=[]),
):
    service = InvestigationService()

    state, pieces = service.start(
        question=q,
        personalities=personality,
    )

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
            "pieces": pieces,
            "personalities": personalities,
            "remove_personality_urls": remove_personality_urls,
        },
    )
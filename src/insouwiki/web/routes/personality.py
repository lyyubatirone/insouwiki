from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from insouwiki.web.services.personality_service import PersonalityService

router = APIRouter()

templates = Jinja2Templates(
    directory="src/insouwiki/web/templates"
)

personality_service = PersonalityService()


@router.get("/personnalites/jean-luc-melenchon")
def jean_luc_melenchon(request: Request):
    personality = personality_service.get_personality(
        "jean-luc-melenchon"
    )

    return templates.TemplateResponse(
        request=request,
        name="personality.html",
        context={
            "personality": personality,
        },
    )
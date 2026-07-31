from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from insouwiki.consultation.documentary_library import (
    DocumentaryLibrary,
)
from insouwiki.web.services.personality_service import (
    PersonalityService,
)


router = APIRouter()

templates = Jinja2Templates(
    directory="src/insouwiki/web/templates",
)

personality_service = PersonalityService()


@router.get("/personnalites")
def personalities(
    request: Request,
):
    library = DocumentaryLibrary()

    personalities = library.list_personalities()

    return templates.TemplateResponse(
        request=request,
        name="personalities.html",
        context={
            "personalities": personalities,
        },
    )


@router.get("/personnalites/{slug}")
def personality(
    request: Request,
    slug: str,
):
    library = DocumentaryLibrary()

    personality = personality_service.get_personality(
        slug,
    )

    documents = library.documents_for_personality(
        slug,
    )

    return templates.TemplateResponse(
        request=request,
        name="personality.html",
        context={
            "personality": personality,
            "documents": documents,
        },
    )
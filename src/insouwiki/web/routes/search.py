from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from insouwiki.web.services.search_service import SearchService

router = APIRouter()

templates = Jinja2Templates(
    directory="src/insouwiki/web/templates"
)


@router.get("/search")
def search(
    request: Request,
    q: str = "",
):
    service = SearchService()

    results = service.search(q)

    return templates.TemplateResponse(
    request=request,
    name="search.html",
    context={
        "query": q,
        "results": results,
    },
)
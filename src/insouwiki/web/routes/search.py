from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(
    directory="src/insouwiki/web/templates"
)


@router.get("/search")
def search(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="search.html",
    )
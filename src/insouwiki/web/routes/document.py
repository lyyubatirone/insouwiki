from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from insouwiki.consultation.documentary_library import DocumentaryLibrary

router = APIRouter()

templates = Jinja2Templates(
    directory="src/insouwiki/web/templates"
)

documentary_library = DocumentaryLibrary()


@router.get("/documents/{permanent_id}")
def document(
    request: Request,
    permanent_id: str,
):
    document = documentary_library.get_document(
        permanent_id
    )

    return templates.TemplateResponse(
        request=request,
        name="document.html",
        context={
            "document": document,
        },
    )
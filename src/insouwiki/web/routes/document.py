from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from insouwiki.consultation.documentary_library import (
    DocumentaryLibrary,
)


router = APIRouter()

templates = Jinja2Templates(
    directory="src/insouwiki/web/templates",
)


def get_documentary_library() -> DocumentaryLibrary:
    return DocumentaryLibrary()


@router.get("/documents/{permanent_id}")
def document(
    request: Request,
    permanent_id: str,
    documentary_library: DocumentaryLibrary = Depends(
        get_documentary_library,
    ),
):
    current_document = documentary_library.get_document(
        permanent_id,
    )

    notice = documentary_library.get_documentary_notice(
        permanent_id,
    )

    transcription = documentary_library.get_transcription(
        permanent_id,
    )

    sequences = documentary_library.get_sequences(
        permanent_id,
    )

    facts = documentary_library.get_documentary_fact_views(
        permanent_id,
    )

    return templates.TemplateResponse(
        request=request,
        name="document.html",
        context={
            "document": current_document,
            "notice": notice,
            "transcription": transcription,
            "sequences": sequences,
            "facts": facts,
        },
    )
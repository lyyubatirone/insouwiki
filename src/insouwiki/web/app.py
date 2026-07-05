from fastapi import FastAPI

from insouwiki.web.routes.home import router as home_router
from insouwiki.web.routes.personality import router as personality_router
from insouwiki.web.routes.search import router as search_router
from insouwiki.web.routes.document import router as document_router



app = FastAPI(
    title="InsouWiki",
)

app.include_router(home_router)
app.include_router(search_router)
app.include_router(personality_router)
app.include_router(document_router)
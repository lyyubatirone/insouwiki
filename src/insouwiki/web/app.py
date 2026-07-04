from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="InsouWiki",
)

templates = Jinja2Templates(
    directory="src/insouwiki/web/templates"
)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
    )
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="InsouWiki",
)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!doctype html>
    <html lang="fr">
        <head>
            <meta charset="utf-8">
            <title>InsouWiki</title>
        </head>
        <body>
            <h1>Bienvenue sur InsouWiki</h1>
            <p>Le premier mur est debout.</p>
        </body>
    </html>
    """
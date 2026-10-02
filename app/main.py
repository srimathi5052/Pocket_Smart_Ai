from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from app.config import (
    STATIC_DIR,
    TEMPLATES_DIR,
    settings,
)
from app.db import init_db
from app.routers import api, auth, pages


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs when the application starts.
    """

    init_db()

    yield


app = FastAPI(
    title="PocketSmart AI",
    version="1.0.0",
    description=(
        "AI-powered budget and recommendation assistant "
        "for home interiors, parties and jewelry."
    ),
    lifespan=lifespan,
)


app.add_middleware(
    SessionMiddleware,
    secret_key=settings.secret_key,
    max_age=60 * 60 * 24 * 7,
    same_site="lax",
    https_only=False,
)


app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)


app.state.templates = Jinja2Templates(
    directory=TEMPLATES_DIR
)


app.include_router(pages.router)
app.include_router(auth.router)
app.include_router(api.router)


@app.get("/startup")
async def startup_status():
    return {
        "status": "ready",
        "application": "PocketSmart AI",
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "gemini_configured": bool(
            settings.gemini_api_key
        ),
        "model": settings.gemini_model,
    }


@app.exception_handler(404)
async def not_found(
    request: Request,
    exc,
):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=404,
            content={
                "detail": "Endpoint not found."
            },
        )

    return app.state.templates.TemplateResponse(
        request,
        "404.html",
        {
            "message": "Page not found."
        },
        status_code=404,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
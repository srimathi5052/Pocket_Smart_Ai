from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/")
async def index(request: Request):
    return request.app.state.templates.TemplateResponse(
        request,
        "index.html",
        {"title": "PocketSmart AI"},
    )


@router.get("/login")
async def login_page(request: Request):
    return request.app.state.templates.TemplateResponse(
        request,
        "login.html",
        {"title": "Login - PocketSmart AI"},
    )


@router.get("/dashboard")
async def dashboard(request: Request):
    return request.app.state.templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "title": "Dashboard - PocketSmart AI",
            "welcome_message": "Welcome back!",
        },
    )

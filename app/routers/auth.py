from fastapi import APIRouter

from app.models import LoginRequest

router = APIRouter(prefix="/auth")


@router.get("/status")
async def auth_status():
    return {"authenticated": False, "message": "Guest mode"}


@router.post("/login")
async def login(payload: LoginRequest):
    return {
        "message": "Login successful",
        "email": payload.email,
        "status": "authenticated",
    }

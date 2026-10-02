from typing import Literal, Optional

from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(..., min_length=3)
    password: str = Field(..., min_length=6)


class RecommendationRequest(BaseModel):
    category: Literal["home_interior", "party", "jewelry"] = "home_interior"
    budget: float = Field(..., gt=0)
    style: str = "modern"
    notes: Optional[str] = None


class RecommendationResponse(BaseModel):
    category: str
    budget: float
    style: str
    recommendation: str
    estimated_cost: float

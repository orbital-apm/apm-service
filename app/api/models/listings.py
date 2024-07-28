from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class GenerateListing(BaseModel):  # type: ignore[misc]
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=1000)
    condition: int = Field(..., ge=1, le=5)
    part_type: list[str]
    price: float = Field(..., gt=0)


class ListingsResponse(GenerateListing):
    id: UUID
    user_id: UUID
    created_at: datetime

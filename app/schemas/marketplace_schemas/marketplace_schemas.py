from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID


class ListingsSchema(BaseModel):
    id: UUID
    title: Optional[str] = None
    description: Optional[str] = None
    condition: Optional[int] = None
    part_type: Optional[list[str]] = None
    price: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)

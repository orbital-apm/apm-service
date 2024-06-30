from pydantic import BaseModel
from uuid import UUID


class GenerateBuild(BaseModel):  # type: ignore[misc]
    build_name: str
    switch_id: UUID
    kit_id: UUID
    keycap_id: UUID
    lubricant_id: UUID

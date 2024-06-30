from pydantic import BaseModel
from uuid import UUID


class GenerateBuild(BaseModel):  # type: ignore[misc]
    build_name: str | None
    switch_id: UUID | None
    kit_id: UUID | None
    keycap_id: UUID | None
    lubricant_id: UUID | None

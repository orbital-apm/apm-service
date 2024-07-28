from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from uuid import UUID


class KeycapSchema(BaseModel):  # type: ignore[misc]
    price: Optional[float] = None
    id: UUID
    vendor: Optional[List[str]] = None
    colors: Optional[List[str]] = None
    layout: Optional[List[str]] = None
    profile: Optional[List[str]] = None
    availability: Optional[bool] = None
    manufacturer: Optional[str] = None
    name: Optional[str] = None
    material: Optional[str] = None
    img_url: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class SwitchSchema(BaseModel):  # type: ignore[misc]
    price: Optional[float] = None
    id: UUID
    vendor: Optional[List[str]] = None
    actuation_force: Optional[float] = None
    travel_distance: Optional[float] = None
    availability: Optional[bool] = None
    manufacturer: Optional[str] = None
    name: Optional[str] = None
    img_url: Optional[str] = None
    switch_type: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class KitsSchema(BaseModel):  # type: ignore[misc]
    id: UUID
    name: Optional[str] = None
    price: Optional[float] = None
    manufacturer: Optional[str] = None
    vendor: Optional[List[str]] = None

    layout_size: Optional[List[str]] = None
    layout_standard: Optional[List[str]] = None
    layout_ergonomic: Optional[str] = None

    hotswappable: Optional[bool] = None
    knob_support: Optional[bool] = None
    rgb_support: Optional[bool] = None
    display_support: Optional[bool] = None

    connection: Optional[List[str]] = None
    mount_style: Optional[str] = None
    material: Optional[str] = None

    availability: Optional[bool] = None
    img_url: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class LubricantsSchema(BaseModel):  # type: ignore[misc]
    id: UUID
    name: Optional[str] = None
    price: Optional[float] = None
    img_url: Optional[str] = None
    availability: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)

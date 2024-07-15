from typing import Optional
from pydantic import BaseModel
from fastapi import Query
from fastapi_filter.contrib.sqlalchemy import Filter
from app.db.models.builder import Keycap, Switch, Kits, Lubricant, Builds


class KeycapFilter(Filter):  # type: ignore[misc]
    vendor: Optional[list[str]] = Query(None)
    vendor__in: Optional[list[str]] = Query(None)
    layout: Optional[list[str]] = Query(None)
    layout__in: Optional[list[str]] = Query(None)
    material: Optional[str] = Query(None)
    profile: Optional[list[str]] = Query(None)
    profile__in: Optional[list[str]] = Query(None)
    custom_order_by: Optional[list[str]] = Query(None)
    custom_search: Optional[str] = None

    class Constants:
        model = Keycap
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["name", "manufacturer", "material"]

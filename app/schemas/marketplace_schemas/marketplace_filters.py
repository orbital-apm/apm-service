from typing import Optional
from pydantic import field_validator
from fastapi import Query
from uuid import UUID
from fastapi_filter.contrib.sqlalchemy import Filter
from app.db.models.marketplace import Listings


class ListingsFilter(Filter): # type: ignore[misc]
    part_type: Optional[list[str]] = None
    user_id: Optional[UUID] = None
    custom_order_by: Optional[list[str]] = Query(None)
    custom_search: Optional[str] = None

    class Constants(Filter.Constants):
        model = Listings
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["title"]

    @field_validator('part_type', mode='before')
    @classmethod
    def split_str_to_list(cls, value: Optional[list[str] | str]) -> Optional[list[str]]:
        if isinstance(value, str):
            return [item.strip() for item in value.split(',')]
        return value
        

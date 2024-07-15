from typing import Optional
from pydantic import field_validator
from fastapi import Query
from fastapi_filter.contrib.sqlalchemy import Filter
from app.db.models.builder import Keycap, Switch, Kits


class KeycapFilter(Filter):  # type: ignore[misc]
    vendor: Optional[list[str]] = Query(None)
#   vendor__in: Optional[list[str]] = Query(None)
    layout: Optional[list[str]] = Query(None)
#   layout__in: Optional[list[str]] = Query(None)
    material: Optional[str] = Query(None)
    profile: Optional[list[str]] = Query(None)
#   profile__in: Optional[list[str]] = Query(None)
    availability: Optional[bool] = None
    custom_order_by: Optional[list[str]] = Query(None)
    custom_search: Optional[str] = None

    class Constants(Filter.Constants):
        model = Keycap
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ["name", "manufacturer", "material"]

    @field_validator('layout', 'profile', 'vendor', mode='before')
    @classmethod
    def split_str_to_list(cls, value: Optional[list[str] | str]) -> Optional[list[str]]:
        if isinstance(value, str):
            return [item.strip() for item in value.split(',')]
        return value


class SwitchFilter(Filter):  # type: ignore[misc]
    switch_type: Optional[str] = None
    vendor: Optional[list[str]] = None
#   vendor__in: Optional[list[str]] = None
    manufacturer: Optional[str] = None
    availability: Optional[bool] = None
    custom_order_by: Optional[list[str]] = Query(None)
    custom_search: Optional[str] = None

    class Constants:
        model = Switch
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ['name', 'manufacturer', 'switch_type']

    @field_validator('vendor', mode='before')
    @classmethod
    def split_str_to_list(cls, value: Optional[list[str] | str]) -> Optional[list[str]]:
        if isinstance(value, str):
            return [item.strip() for item in value.split(',')]
        return value


class KitsFilter(Filter):  # type: ignore[misc]
    vendor: Optional[list[str]] = None
#   vendor__in: Optional[list[str]] = None
    manufacturer: Optional[str] = None
    layout_size: Optional[list[str]] = None
#   layout_size__in: Optional[list[str]] = None
    layout_standard: Optional[list[str]] = None
#   layout_standard__in: Optional[list[str]] = None
    layout_ergonomic: Optional[str] = None
    hotswappable: Optional[bool] = None
    knob_support: Optional[bool] = None
    rgb_support: Optional[bool] = None
    display_support: Optional[bool] = None
    connection: Optional[list[str]] = None
#   connection__in: Optional[list[str]] = None
    material: Optional[str] = None
    availability: Optional[bool] = None

    custom_order_by: Optional[list[str]] = Query(None)
    custom_search: Optional[str] = None

    class Constants:
        model = Kits
        ordering_field_name = "custom_order_by"
        search_field_name = "custom_search"
        search_model_fields = ['name', 'manufacturer', 'layout_size', 'layout_standard', 'connection']

    @field_validator('layout_size', 'layout_standard', 'connection', mode='before')
    @classmethod
    def split_str_to_list(cls, value: Optional[list[str] | str]) -> Optional[list[str]]:
        if isinstance(value, str):
            return [item.strip() for item in value.split(',')]
        return value

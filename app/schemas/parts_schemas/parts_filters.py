from typing import Optional
from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter


class KeycapFilter(Filter):  # type: ignore[misc]
    vendor: Optional[list[str]] = None
    vendor_in: Optional[list[str]] = None
    layout: Optional[list[str]] = None
    layout_in: Optional[list[str]] = None
    material: Optional[str] = None
    profile: Optional[list[str]] = None
    
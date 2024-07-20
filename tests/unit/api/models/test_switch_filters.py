import pytest
from pydantic import ValidationError

from app.schemas.parts_schemas.parts_filters import SwitchFilter


@pytest.fixture
def switch_filter() -> SwitchFilter:
    return SwitchFilter()

# Positive Unit Testing


def test_switch_type_filter(switch_filter: SwitchFilter) -> None:
    switch_filter.switch_type = "Linear"
    assert switch_filter.switch_type == "Linear"


def test_vendor_filter(switch_filter: SwitchFilter) -> None:
    switch_filter.vendor = ["Vendor-1", "Vendor-2"]
    assert switch_filter.vendor == ["Vendor-1", "Vendor-2"]


def test_manufacturer_filter(switch_filter: SwitchFilter) -> None:
    switch_filter.manufacturer = "Manufacturer-1"
    assert switch_filter.manufacturer == "Manufacturer-1"


def test_availability_filter(switch_filter: SwitchFilter) -> None:
    switch_filter.availability = True
    assert switch_filter.availability is True


def test_custom_order_by(switch_filter: SwitchFilter) -> None:
    switch_filter.custom_order_by = ["name", "-price"]
    assert switch_filter.custom_order_by == ["name", "-price"]


def test_custom_search(switch_filter: SwitchFilter) -> None:
    switch_filter.custom_search = "Cherry MX Red"
    assert switch_filter.custom_search == "Cherry MX Red"

# Negative Unit Testing


def test_invalid_switch_type_filter(switch_filter: SwitchFilter) -> None:
    with pytest.raises(ValidationError):
        SwitchFilter(switch_type=1)


def test_invalid_vendor_filter(switch_filter: SwitchFilter) -> None:
    with pytest.raises(ValidationError):
        SwitchFilter(vendor=1)


def test_invalid_manufacturer_filter(switch_filter: SwitchFilter) -> None:
    with pytest.raises(ValidationError):
        SwitchFilter(manufacturer=1)


def test_invalid_availability_filter(switch_filter: SwitchFilter) -> None:
    with pytest.raises(ValidationError):
        SwitchFilter(availability="Available")


def test_invalid_custom_order_by(switch_filter: SwitchFilter) -> None:
    with pytest.raises(ValidationError):
        SwitchFilter(custom_order_by="invalid")


def test_invalid_custom_search(switch_filter: SwitchFilter) -> None:
    with pytest.raises(ValidationError):
        SwitchFilter(custom_search=1)

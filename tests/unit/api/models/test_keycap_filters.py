import pytest
from pydantic import ValidationError

from app.schemas.parts_schemas.parts_filters import KeycapFilter


@pytest.fixture
def keycap_filter() -> KeycapFilter:
    return KeycapFilter()

# Positive Unit Testing


def test_vendor_filter(keycap_filter: KeycapFilter) -> None:
    keycap_filter.vendor = ["Vendor-1", "Vendor-2"]
    assert keycap_filter.vendor == ["Vendor-1", "Vendor-2"]


def test_layout_filter(keycap_filter: KeycapFilter) -> None:
    keycap_filter.layout = ["ANSI", "OEM"]
    assert keycap_filter.layout == ["ANSI", "OEM"]


def test_material__in_filter(keycap_filter: KeycapFilter) -> None:
    keycap_filter.material__in = ["ABS"]
    assert keycap_filter.material__in == ["ABS"]


def test_profile_filter(keycap_filter: KeycapFilter) -> None:
    keycap_filter.profile = ["Cherry", "OEM"]
    assert keycap_filter.profile == ["Cherry", "OEM"]


def test_availability_filter(keycap_filter: KeycapFilter) -> None:
    keycap_filter.availability = True
    assert keycap_filter.availability is True


def test_custom_order_by(keycap_filter: KeycapFilter) -> None:
    keycap_filter.custom_order_by = ["name", "-price"]
    assert keycap_filter.custom_order_by == ["name", "-price"]


def test_custom_search(keycap_filter: KeycapFilter) -> None:
    keycap_filter.custom_search = "Cherry PBT"
    assert keycap_filter.custom_search == "Cherry PBT"

# Negative Unit Testing


def test_invalid_vendor_filter(keycap_filter: KeycapFilter) -> None:
    with pytest.raises(ValidationError):
        KeycapFilter(vendor=1)


def test_invalid_layout_filter(keycap_filter: KeycapFilter) -> None:
    with pytest.raises(ValidationError):
        KeycapFilter(layout=1)


def test_invalid_material__in_filter(keycap_filter: KeycapFilter) -> None:
    with pytest.raises(ValidationError):
        KeycapFilter(material__in=1)


def test_invalid_profile_filter(keycap_filter: KeycapFilter) -> None:
    with pytest.raises(ValidationError):
        KeycapFilter(profile=1)


def test_invalid_availability_filter(keycap_filter: KeycapFilter) -> None:
    with pytest.raises(ValidationError):
        KeycapFilter(availability="Available")


def test_invalid_custom_order_by(keycap_filter: KeycapFilter) -> None:
    with pytest.raises(ValidationError):
        KeycapFilter(custom_order_by="invalid")


def test_invalid_custom_search(keycap_filter: KeycapFilter) -> None:
    with pytest.raises(ValidationError):
        KeycapFilter(custom_search=1)

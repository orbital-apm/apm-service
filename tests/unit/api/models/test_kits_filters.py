import pytest
from pydantic import ValidationError

from app.schemas.parts_schemas.parts_filters import KitsFilter


@pytest.fixture
def kits_filter() -> KitsFilter:
    return KitsFilter()

# Positive Unit Testing


def test_vendor_filter(kits_filter: KitsFilter) -> None:
    kits_filter.vendor = ["Vendor-1", "Vendor-2"]
    assert kits_filter.vendor == ["Vendor-1", "Vendor-2"]


def test_manufacturer_filter(kits_filter: KitsFilter) -> None:
    kits_filter.manufacturer__in = ["Manufacturer-1"]
    assert kits_filter.manufacturer__in == ["Manufacturer-1"]


def test_layout_size_filter(kits_filter: KitsFilter) -> None:
    kits_filter.layout_size = ["60%", "TKL"]
    assert kits_filter.layout_size == ["60%", "TKL"]


def test_layout_standard_filter(kits_filter: KitsFilter) -> None:
    kits_filter.layout_standard = ["ANSI", "ISO"]
    assert kits_filter.layout_standard == ["ANSI", "ISO"]


def test_layout_ergonomic_filter(kits_filter: KitsFilter) -> None:
    kits_filter.layout_ergonomic__in = ["Split"]
    assert kits_filter.layout_ergonomic__in == ["Split"]


def test_hotswappable_filter(kits_filter: KitsFilter) -> None:
    kits_filter.hotswappable__in = [True]
    assert kits_filter.hotswappable__in == [True]


def test_knob_support_filter(kits_filter: KitsFilter) -> None:
    kits_filter.knob_support__in = [True]
    assert kits_filter.knob_support__in == [True]


def test_rgb_support_filter(kits_filter: KitsFilter) -> None:
    kits_filter.rgb_support__in = [True]
    assert kits_filter.rgb_support__in == [True]


def test_display_support_filter(kits_filter: KitsFilter) -> None:
    kits_filter.display_support__in = [True]
    assert kits_filter.display_support__in == [True]


def test_connection_filter(kits_filter: KitsFilter) -> None:
    kits_filter.connection = ["USB-C", "Bluetooth"]
    assert kits_filter.connection == ["USB-C", "Bluetooth"]


def test_material_filter(kits_filter: KitsFilter) -> None:
    kits_filter.material__in = ["Aluminum"]
    assert kits_filter.material__in == ["Aluminum"]


def test_availability_filter(kits_filter: KitsFilter) -> None:
    kits_filter.availability__in = [True]
    assert kits_filter.availability__in == [True]


def test_custom_order_by(kits_filter: KitsFilter) -> None:
    kits_filter.custom_order_by = ["name", "-price"]
    assert kits_filter.custom_order_by == ["name", "-price"]


def test_custom_search(kits_filter: KitsFilter) -> None:
    kits_filter.custom_search = "60% Aluminum Kit"
    assert kits_filter.custom_search == "60% Aluminum Kit"

# Negative Unit Testing


def test_invalid_vendor_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(vendor=1)


def test_invalid_manufacturer_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(manufacturer__in=1)


def test_invalid_layout_size_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(layout_size=1)


def test_invalid_layout_standard_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(layout_standard=1)


def test_invalid_layout_ergonomic_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(layout_ergonomic__in=1)


def test_invalid_hotswappable_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(hotswappable__in="invalid")


def test_invalid_knob_support_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(knob_support__in="invalid")


def test_invalid_rgb_support_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(rgb_support__in="invalid")


def test_invalid_display_support_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(display_support__in="invalid")


def test_invalid_connection_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(connection=1)


def test_invalid_material_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(material__in=1)


def test_invalid_availability_filter(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(availability__in="Available")


def test_invalid_custom_order_by(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(custom_order_by="invalid")


def test_invalid_custom_search(kits_filter: KitsFilter) -> None:
    with pytest.raises(ValidationError):
        KitsFilter(custom_search=1)

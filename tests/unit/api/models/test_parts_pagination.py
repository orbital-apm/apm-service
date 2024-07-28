import pytest
from uuid import uuid4
from pydantic import ValidationError

from app.schemas.parts_schemas.parts import KeycapSchema, SwitchSchema, KitsSchema, LubricantsSchema


def test_valid_keycap_schema() -> None:
    keycap_data = {
        "price": 100.0,
        "id": uuid4(),
        "vendor": ["Vendor-1", "Vendor-2"],
        "colors": ["Red", "Blue", "Yellow"],
        "layout": ["ANSI", "ISO"],
        "profile": ["Cherry", "OEM"],
        "availability": True,
        "manufacturer": "Manufacturer-1",
        "name": "Unit Test Keycap",
        "material": "PBT",
        "img_url": "http://unit-test-link.com/image.jpg"
    }
    keycap = KeycapSchema(**keycap_data)
    assert keycap.model_dump() == keycap_data


def test_invalid_keycap_schema() -> None:
    with pytest.raises(ValidationError):
        KeycapSchema(id=None)


def test_valid_switch_schema() -> None:
    switch_data = {
        "id": uuid4(),
        "price": 0.5,
        "vendor": ["Vendor-1"],
        "actuation_force": 45.0,
        "travel_distance": 4.0,
        "availability": True,
        "manufacturer": "Manufacturer-1",
        "name": "Unit Test Switch",
        "img_url": "http://unit-test-link.com/image.jpg",
        "switch_type": "Linear"
    }
    switch = SwitchSchema(**switch_data)
    assert switch.model_dump() == switch_data


def test_switch_schema_invalid() -> None:
    with pytest.raises(ValidationError):
        SwitchSchema(id=None, actuation_force="0.40")


def test_valid_kits_schema() -> None:
    kits_data = {
        "id": uuid4(),
        "name": "Unit Test Kit",
        "price": 150.0,
        "manufacturer": "Manufacturer-1",
        "vendor": ["Vendor-1", "Vendor-2"],
        "layout_size": ["60%", "TKL"],
        "layout_standard": ["ANSI"],
        "layout_ergonomic": "Split",
        "hotswappable": True,
        "knob_support": False,
        "rgb_support": True,
        "display_support": False,
        "connection": ["USB-C", "Bluetooth"],
        "mount_style": "Gasket",
        "material": "Aluminum",
        "availability": True,
        "img_url": "http://unit-test-link.com/image.jpg"
    }
    kit = KitsSchema(**kits_data)
    assert kit.model_dump() == kits_data


def test_kits_schema_invalid() -> None:
    with pytest.raises(ValidationError):
        KitsSchema(id=None, price="150.0")


def test_lubricants_schema_valid() -> None:
    lubricant_data = {
        "id": uuid4(),
        "name": "Unit Test Lubrication",
        "price": 10.0,
        "img_url": "http://unit-test-link.com/image.jpg",
        "availability": True
    }
    lubricant = LubricantsSchema(**lubricant_data)
    assert lubricant.model_dump() == lubricant_data


def test_lubricants_schema_invalid() -> None:
    with pytest.raises(ValidationError):
        LubricantsSchema(id=None, price="10.0")

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from typing import Generator
from uuid import uuid4

from app.main import app
from app.db.models.builder import Keycap

client = TestClient(app)

FAKE_KEYCAPS = [
    Keycap(id=uuid4(), name="Keycap1", vendor=["Vendor1"], layout=["ANSI"], material="ABS", profile=["Cherry"], availability=True,
           price=10.9),
    Keycap(id=uuid4(), name="Keycap2", vendor=["Vendor2"], layout=["ISO","ANSI"], material="PBT", profile=["OEM"], availability=False,
           price=20.4),
    Keycap(id=uuid4(), name="Keycap3", vendor=["Vendor1"], layout=["ANSI"], material="PBT", profile=["MAO"], availability=True,
           price=15.5),
    Keycap(id=uuid4(), name="Keycap4", vendor=["Vendor3"], layout=["ANSI"], material="ABS", profile=["NSA"], availability=True,
           price=25.2),
    Keycap(id=uuid4(), name="Keycap5", vendor=["Vendor2"], layout=["ISO"], material="ABS", profile=["Cherry"], availability=False,
           price=30.1),
]


@pytest.fixture(autouse=True)
def mock_db_query() -> Generator[MagicMock, None, None]:
    with patch('app.db.crud.get_keycaps') as test_get_keycaps:
        test_get_keycaps.return_value = FAKE_KEYCAPS
        yield test_get_keycaps


def test_keycap_filter_valid_vendor() -> None:
    response = client.get("/v1/parts/keycaps?vendor=Vendor1")

    assert response.status_code == 200


def test_keycap_filter_invalid_vendor() -> None:
    response = client.get("/v1/parts/keycaps?vendor=Vendor4")

    assert response.status_code == 404


def test_keycap_filter_multiple_vendors() -> None:  # Expected behaviour: To return the item that has BOTH vendors
    response = client.get("/v1/parts/keycaps?vendor=Vendor1,Vendor2")

    assert response.status_code == 200


def test_keycap_filter_layout() -> None:
    response = client.get("/v1/parts/keycaps?layout=ANSI")

    assert response.status_code == 200


def test_keycap_filter_material() -> None:
    response = client.get("/v1/parts/keycaps?material__in=ABS")

    assert response.status_code == 200



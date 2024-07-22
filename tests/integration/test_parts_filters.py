import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from typing import Generator
from uuid import uuid4

from app.main import app
from app.db.models.builder import Keycap

client = TestClient(app)


def test_keycap_filter_valid_vendor() -> None:
    response = client.get("/v1/parts/keycaps?vendor=Epomaker")

    assert response.status_code == 200
    data = response.json()
    print(data.items)
    assert len(data.items) == 1


def test_keycap_filter_invalid_vendor() -> None:
    response = client.get("/v1/parts/keycaps?vendor=Akko")

    assert response.status_code == 200
    data = response.json()
    print(data)
    assert len(data) == 0


def test_keycap_filter_multiple_vendors() -> None:  # Expected behaviour: To return the item that has BOTH vendors
    response = client.get("/v1/parts/keycaps?vendor=Vendor1,Vendor2")

    assert response.status_code == 200


def test_keycap_filter_layout() -> None:
    response = client.get("/v1/parts/keycaps?layout=ANSI")

    assert response.status_code == 200


def test_keycap_filter_material() -> None:
    response = client.get("/v1/parts/keycaps?material__in=ABS")

    assert response.status_code == 200


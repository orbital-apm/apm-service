from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_switches_valid_all() -> None:
    response = client.get("/v1/parts/switches")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 3


def test_pagination() -> None:
    response = client.get("/v1/parts/switches")

    assert response.status_code == 200
    data = response.json()
    assert "page" in data


def test_switches_filter_invalid_vendor() -> None:
    response = client.get("/v1/parts/switches?vendor=Glorious")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_switches_filter_multiple_vendors() -> None:  # Expected behaviour: To return the item that has BOTH vendors
    response = client.get("/v1/parts/switches?vendor=MK,Dangkeebs")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_switches_filter_valid_switch_type() -> None:
    response = client.get("/v1/parts/switches?switch_type=Linear")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_switches_filter_invalid_switch_type() -> None:
    response = client.get("/v1/parts/switches?switch_type=Silent")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_switches_filter_valid_manufacturer() -> None:
    response = client.get("/v1/parts/switches?manufacturer=Ktt")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_switches_filter_invalid_manufacturer() -> None:
    response = client.get("/v1/parts/switches?manufacturer=invalid")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_switches_filter_valid_availability() -> None:
    response = client.get("/v1/parts/switches?availability=True")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 2


def test_switches_filter_invalid_availability() -> None:
    response = client.get("/v1/parts/switches?availability=1313")

    assert response.status_code == 422

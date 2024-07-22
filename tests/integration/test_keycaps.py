from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_keycaps_valid_all() -> None:
    response = client.get("/v1/parts/keycaps")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 3


def test_pagination() -> None:
    response = client.get("/v1/parts/keycaps")

    assert response.status_code == 200
    data = response.json()
    assert "page" in data


def test_keycap_filter_valid_vendor() -> None:
    response = client.get("/v1/parts/keycaps?vendor=Epomaker")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_keycap_filter_invalid_vendor() -> None:
    response = client.get("/v1/parts/keycaps?vendor=Akko")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_keycap_filter_multiple_vendors() -> None:  # Expected behaviour: To return the item that has BOTH vendors
    response = client.get("/v1/parts/keycaps?vendor=ZFrontier,Diykeycap")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1  # S


def test_keycap_filter_valid_layout() -> None:
    response = client.get("/v1/parts/keycaps?layout=ANSI")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_keycap_filter_invalid_layout() -> None:
    response = client.get("/v1/parts/keycaps?layout=Cherry")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_keycap_filter_multiple_layouts() -> None:  # Todo: Add data for MULTIPLE LAYOUTS
    response = client.get("/v1/parts/keycaps?layout=ANSI,ISO")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_keycap_filter_valid_material__in() -> None:  # Expected behaviour: To return items
    response = client.get("/v1/parts/keycaps?material__in=ABS,PC")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 2


def test_keycap_filter_valid_profile() -> None:
    response = client.get("/v1/parts/keycaps?profile=Cherry")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 2


def test_keycap_filter_invalid_profile() -> None:
    response = client.get("/v1/parts/keycaps?profile=invalid-profile")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_keycap_filter_multiple_profiles() -> None:  # Todo: Add data to fulfill this test
    response = client.get("/v1/parts/keycaps?profile=Cherry,NSA")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_keycap_filter_valid_availability() -> None:
    response = client.get("/v1/parts/keycaps?availability=True")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 2


def test_keycap_filter_invalid_availability() -> None:  # Todo: Fix this code
    response = client.get("/v1/parts/keycaps?availability=2")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0

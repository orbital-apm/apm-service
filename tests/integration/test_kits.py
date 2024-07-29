from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_kits_valid_all() -> None:
    response = client.get("/v1/parts/kits")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 4


def test_pagination() -> None:
    response = client.get("/v1/parts/kits")

    assert response.status_code == 200
    data = response.json()
    assert "page" in data


def test_kits_filter_valid_vendor() -> None:
    response = client.get("/v1/parts/kits?vendor=Keychron")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_kits_filter_invalid_vendor() -> None:
    response = client.get("/v1/parts/kits?vendor=Glorious")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


# def test_kits_filter_multiple_vendors() -> None:  # Expected behaviour: To return the item that has BOTH vendors
#     response = client.get("/v1/parts/kits?vendor=KBDFans,Keychron")

#     assert response.status_code == 200
#     data = response.json()
#     assert len(data['items']) == 1


def test_kits_filter_valid_layout_size() -> None:
    response = client.get("/v1/parts/kits?layout_size=100%")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_kits_filter_invalid_layout_size() -> None:
    response = client.get("/v1/parts/kits?layout_size=invalid-layout-size")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_kits_filter_multiple_layout_sizes() -> None:  # Todo: Add data for MULTIPLE LAYOUTS
    response = client.get("/v1/parts/kits?layout_size=65%,Split")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_kits_filter_valid_layout_standard() -> None:
    response = client.get("/v1/parts/kits?layout_standard=ANSI")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 2


def test_kits_filter_invalid_layout_standard() -> None:
    response = client.get("/v1/parts/kits?layout_standard=invalid")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_kits_filter_multiple_layout_standards() -> None:  # Todo: Add data for MULTIPLE LAYOUT STANDARDS
    response = client.get("/v1/parts/kits?layout_standard=ANSI,Ortholinear")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_kits_filter_valid_layout_ergonomic() -> None:
    response = client.get("/v1/parts/kits?layout_ergonomic__in=Southpaw")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_kits_filter_invalid_layout_ergonomic() -> None:
    response = client.get("/v1/parts/kits?layout_ergonomic__in=Northpaw")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_kits_filter_valid_hotswappable() -> None:
    response = client.get("/v1/parts/kits?hotswappable__in=true")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 3


def test_kits_filter_invalid_hotswappable() -> None:
    response = client.get("/v1/parts/kits?hotswappable__in=2")

    assert response.status_code == 422


def test_kits_filter_valid_knob_support() -> None:
    response = client.get("/v1/parts/kits?knob_support__in=False")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 4


def test_kits_filter_invalid_knob_support() -> None:
    response = client.get("/v1/parts/kits?knob_support__in=Flse")

    assert response.status_code == 422


def test_kits_filter_valid_rgb_support() -> None:
    response = client.get("/v1/parts/kits?rgb_support__in=False")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_kits_filter_invalid_rgb_support() -> None:
    response = client.get("/v1/parts/kits?rgb_support__in=Flse")

    assert response.status_code == 422


def test_kits_filter_valid_display_support() -> None:
    response = client.get("/v1/parts/kits?display_support__in=False")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 2


def test_kits_filter_invalid_display_support() -> None:
    response = client.get("/v1/parts/kits?display_support__in=Flse")

    assert response.status_code == 422


def test_kits_filter_valid_connection() -> None:
    response = client.get("/v1/parts/kits?connection=Wired")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_kits_filter_invalid_connection() -> None:
    response = client.get("/v1/parts/kits?connection=Wirde")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


# def test_kits_filter_multiple_connections() -> None:
#     response = client.get("/v1/parts/kits?connection=2.4Ghz,Wireless")

#     assert response.status_code == 200
#     data = response.json()
#     assert len(data['items']) == 1


def test_kits_filter_valid_mount_style() -> None:
    response = client.get("/v1/parts/kits?mount_style__in=Tray+Mount")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 2


def test_kits_filter_invalid_mount_style() -> None:
    response = client.get("/v1/parts/kits?mount_style__in=Maglev+Mountain")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_kits_filter_valid_material() -> None:
    response = client.get("/v1/parts/kits?material__in=Metal")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 1


def test_kits_filter_invalid_material() -> None:
    response = client.get("/v1/parts/kits?material__in=invalid")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 0


def test_kits_filter_valid_availability() -> None:
    response = client.get("/v1/parts/kits?availability__in=true")

    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) == 3


def test_kits_filter_invalid_availability() -> None:
    response = client.get("/v1/parts/kits?availability__in=2")

    assert response.status_code == 422

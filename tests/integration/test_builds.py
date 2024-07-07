from fastapi.testclient import TestClient
from app.main import app

ENDPOINT = "/v1/builds/"
FAKE_BUILD_REQUEST = {
    "build_name": "test-build",
    "switch_id": "02c80c98-069d-4771-bb00-802962186574",
    "kit_id": "051db3a8-9ba9-42c9-a58e-b2acc11ffd58",
    "keycap_id": "0208b85c-2b57-4a5a-8e0f-8993bfe9c20c",
    "lubricant_id": "56121e0f-cc68-4d54-a7fd-a28dd19fefd4"
}

client = TestClient(app)


def test_add_build() -> None:
    response = client.post(url=ENDPOINT, json=FAKE_BUILD_REQUEST)

    assert response.status_code == 201


def test_add_invalid_build() -> None:
    invalid_data = {
        "build_name": "test-build",
        "switch_id": "02c80c98-069d-4771-bb00-802962186574"
    }

    response = client.post(url=ENDPOINT, json=invalid_data)
    assert response.status_code == 422


def test_get_valid_build() -> None:
    create_build_response = client.post(url=ENDPOINT, json=FAKE_BUILD_REQUEST)
    assert create_build_response.status_code == 201
    build_id = create_build_response.json()["id"]

    get_response = client.get(f"builds/{build_id}")
    assert get_response.status_code == 200

    build_info = get_response.json()
    assert build_info["id"] == build_id
    assert build_info["build_name"] == FAKE_BUILD_REQUEST["build_name"]


def test_get_invalid_build() -> None:
    response = client.get(url="/builds/13123123")
    assert response.status_code == 404
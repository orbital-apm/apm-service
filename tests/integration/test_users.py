from fastapi.testclient import TestClient

from app.main import app

ENDPOINT = "/v1/users"
FAKE_ADD_USER_REQUEST = {
    "email": "a@b.c",
    "username": "username",
    "password": "password"
}

client = TestClient(app)


def test_add_user() -> None:
    response = client.post(url=ENDPOINT, json=FAKE_ADD_USER_REQUEST)

    assert response.status_code == 201


def test_duplicate_user() -> None:
    client.post(url=ENDPOINT, json=FAKE_ADD_USER_REQUEST)
    response = client.post(url=ENDPOINT, json=FAKE_ADD_USER_REQUEST)

    assert response.status_code == 409

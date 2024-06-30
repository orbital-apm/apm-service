from fastapi.testclient import TestClient

from app.main import app

ENDPOINT = "/v1/auth/token"
FAKE_GENERATE_TOKEN_REQUEST_VALID = {
    "email": "admin@admin.com",
    "password": "password"
}
FAKE_GENERATE_TOKEN_REQUEST_INVALID = {
    "email": "a@b.c",
    "password": "password"
}

client = TestClient(app)


# def test_generate_token_valid() -> None:
#     response = client.post(url=ENDPOINT, json=FAKE_GENERATE_TOKEN_REQUEST_VALID)
#
#     assert response.status_code == 200


def test_generate_token_invalid() -> None:
    response = client.post(url=ENDPOINT, json=FAKE_GENERATE_TOKEN_REQUEST_INVALID)

    assert response.status_code == 401

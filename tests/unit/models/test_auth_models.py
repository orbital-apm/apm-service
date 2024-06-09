import pytest
from pydantic import ValidationError

from app.models.auth_models import TokenRequest


def test_token_request_valid() -> None:
    data = {
        "email": "example@example.com",
        "password": "my_secret_password"
    }
    token_request = TokenRequest(**data)

    assert token_request.email == "example@example.com"
    assert token_request.password == "my_secret_password"


def test_token_request_invalid_email() -> None:
    data = {
        "email": "invalid_email",
        "password": "my_secret_password"
    }

    with pytest.raises(ValidationError):
        TokenRequest(**data)


def test_token_request_missing_email() -> None:
    data = {
        "password": "my_secret_password"
    }

    with pytest.raises(ValidationError):
        TokenRequest(**data)


def test_token_request_missing_password() -> None:
    data = {
        "email": "example@example.com"
    }

    with pytest.raises(ValidationError):
        TokenRequest(**data)


def test_token_request_extra() -> None:
    data = {
        "email": "example@example.com",
        "password": "my_secret_password",
        "hotel": "trivago"
    }
    token_request = TokenRequest(**data)

    assert token_request.email == "example@example.com"
    assert token_request.password == "my_secret_password"
    assert not hasattr(token_request, "hotel")

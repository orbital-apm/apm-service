import pytest
from pydantic import ValidationError

from app.api.models.users import AddUserRequest


def test_user_add_request_valid() -> None:
    data = {
        "email": "example@example.com",
        "username": "example_username",
        "password": "my_secret_password"
    }
    user_add_request = AddUserRequest(**data)

    assert user_add_request.email == "example@example.com"
    assert user_add_request.username == "example_username"
    assert user_add_request.password == "my_secret_password"


def test_user_add_request_invalid_email() -> None:
    data = {
        "email": "invalid_email",
        "username": "example_username",
        "password": "my_secret_password"
    }

    with pytest.raises(ValidationError):
        AddUserRequest(**data)


def test_user_add_request_missing_email() -> None:
    data = {
        "username": "example_username",
        "password": "my_secret_password"
    }

    with pytest.raises(ValidationError):
        AddUserRequest(**data)


def test_token_request_missing_username() -> None:
    data = {
        "email": "example@example.com",
        "password": "my_secret_password"
    }

    with pytest.raises(ValidationError):
        AddUserRequest(**data)


def test_token_request_missing_password() -> None:
    data = {
        "email": "example@example.com",
        "username": "example_username",
    }

    with pytest.raises(ValidationError):
        AddUserRequest(**data)


def test_token_request_extra() -> None:
    data = {
        "email": "example@example.com",
        "username": "example_username",
        "password": "my_secret_password",
        "hotel": "trivago"
    }
    user_add_request = AddUserRequest(**data)

    assert user_add_request.email == "example@example.com"
    assert user_add_request.username == "example_username"
    assert user_add_request.password == "my_secret_password"
    assert not hasattr(user_add_request, "hotel")

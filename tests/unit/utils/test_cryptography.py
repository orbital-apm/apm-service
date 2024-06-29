import bcrypt

from app.utils.cryptography import verify_password, hash_password


def test_hash_password() -> None:
    password = "my_secret_password"
    hashed = hash_password(password)

    assert bcrypt.checkpw(password.encode(), hashed.encode())


def test_verify_password() -> None:
    password = "my_secret_password"
    hashed = hash_password(password)

    assert verify_password(password, hashed) is True
    assert verify_password("not_my_secret_password", hashed) is False

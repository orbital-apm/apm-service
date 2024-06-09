import jwt
import os
import time
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models.user import UserDB
from app.db.repositories.user_repository import UserRepository
from app.models.auth_models import TokenRequest
from app.utils.cryptography import verify_password


def generate_jwt(user: UserDB) -> str:
    time_now = int(time.time())
    claims = {
        "sub": str(user.id),
        "iss": "apm-service",
        "iat": time_now,
        "exp": time_now + (int(os.getenv("ACCESS_TOKEN_VALIDITY_MINUTES", 15)) * 60)
    }

    # Todo: Consolidate env vars. Ensure not None.
    token = jwt.encode(payload=claims, key=os.getenv("ACCESS_TOKEN_SECRET_KEY"), algorithm="HS256")

    return token


def get_token(user: TokenRequest, db: Session) -> str:
    user_repository = UserRepository(db)

    existing_user = user_repository.get_user_by_email(user.email)
    if not existing_user or not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password.")

    access_token = generate_jwt(existing_user)

    return access_token

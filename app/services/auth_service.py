import jwt
import os
import time
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.db.models.user import User
from app.db.repositories.user_repository import UserRepository
from app.schemas.auth import LoginUserSchema, RegisterUserSchema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bool(pwd_context.verify(plain_password, hashed_password))


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def generate_jwt(user: User) -> str:
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


def login_user(returning_user: LoginUserSchema, db: Session) -> str:
    user_repository = UserRepository(db)

    existing_user = user_repository.get_user_by_email(returning_user.email)
    if not existing_user or not verify_password(returning_user.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password.")

    access_token = generate_jwt(existing_user)

    return access_token


def register_user(new_user: RegisterUserSchema, db: Session) -> None:
    user_repository = UserRepository(db)

    existing_user = user_repository.get_user_by_email(new_user.email)
    if existing_user:
        raise HTTPException(status_code=409, detail="Email already in use.")

    user = User(
        username=new_user.username,
        email=new_user.email,
        password=hash_password(new_user.password)
    )
    user_repository.insert_user(user)

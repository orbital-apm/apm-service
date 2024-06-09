from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models.user import UserDB
from app.db.repositories.user_repository import UserRepository
from app.models.users_models import UserAddRequest
from app.utils.cryptography import hash_password


def add_user(user: UserAddRequest, db: Session) -> None:
    user_repository = UserRepository(db)

    existing_user = user_repository.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=409, detail="Email already in use.")

    user = UserDB(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )
    user_repository.insert_user(user)

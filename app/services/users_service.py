from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models.user import UserEntity
from app.db.repositories.user_repository import UserRepository
from app.services.models.users import AddUserParams
from app.utils.cryptography import hash_password


def add_user(params: AddUserParams, db: Session) -> None:
    user_repository = UserRepository(db)

    existing_user = user_repository.get_user_by_email(params.email)
    if existing_user:
        raise HTTPException(status_code=409, detail="Email already in use.")

    params.password = hash_password(params.password)

    user_repository.insert_user(params)

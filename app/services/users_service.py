from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.repositories.user_repository import UserRepository
from app.services.models.users import AddUserParams
from app.utils.cryptography import hash_password


def add_user(params: AddUserParams, db: Session) -> None:
    user_repository = UserRepository(db)

    params.password = hash_password(params.password)

    user_repository.insert_user(params)

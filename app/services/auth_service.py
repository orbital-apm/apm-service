from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.repositories.user_repository import UserRepository
from app.services.models.auth import GenerateTokenParams
from app.utils.cryptography import verify_password, generate_jwt


def get_token(params: GenerateTokenParams, db: Session) -> str:
    user_repository = UserRepository(db)

    existing_user = user_repository.get_user_by_email(params.email)
    if not existing_user or not verify_password(params.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password.")

    access_token = generate_jwt(str(existing_user.id))

    return access_token

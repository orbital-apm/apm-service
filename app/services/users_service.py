from sqlalchemy.orm import Session

from app.db.repositories.user_repository import UserRepository
from app.services.models.users import AddUserParams
from app.utils.cryptography import hash_password, generate_jwt


def add_user(params: AddUserParams, db: Session) -> str:
    user_repository = UserRepository(db)

    params.password = hash_password(params.password)
    user = user_repository.insert_user(params)
    access_token = generate_jwt(str(user.id))

    return access_token

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.models.user import UserEntity
from app.services.models.users import AddUserParams, User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(UserEntity).filter(UserEntity.email == email).first()

    def insert_user(self, params: AddUserParams) -> User:
        try:
            user = UserEntity(**params.model_dump())

            self.db.add(user)
            self.db.commit()

            return User(
                id=str(user.id),
                email=user.email,
                username=user.username,
                password=user.password
            )

        except IntegrityError:
            raise HTTPException(status_code=409, detail="Email/username already in use.")

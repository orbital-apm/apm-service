from sqlalchemy.orm import Session

from app.db.models.user import UserEntity
from app.services.models.users import AddUserParams


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> UserEntity | None:
        return self.db.query(UserEntity).filter(UserEntity.email == email).first()

    def insert_user(self, params: AddUserParams) -> None:
        user = UserEntity(**params.model_dump())

        self.db.add(user)
        self.db.commit()

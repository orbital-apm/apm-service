from sqlalchemy.orm import Session

from app.db.models.user import UserDB


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> UserDB | None:
        return self.db.query(UserDB).filter(UserDB.email == email).first()

    def insert_user(self, user: UserDB) -> None:
        self.db.add(user)
        self.db.commit()

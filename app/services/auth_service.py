from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.api.models.auth_models import RegistrationRequest
from app.schemas.auth import NewUserSchema
from app.db.models.user import User
from app.db.repositories.user_repository import UserRepository


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bool(pwd_context.verify(plain_password, hashed_password))


def get_user(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


def authenticate_user(db: Session, username: str, password: str): # type: ignore
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, str(user.hashed_password)):
        return False
    return user


def register_new_user(new_user: NewUserSchema, db: Session) -> None:
    user_repository = UserRepository(db)
    existing_user = user_repository.get_user_by_email(new_user.email)

    if existing_user:
        raise HTTPException(status_code=409, detail="Email already in use.")

    user = User(
        username=new_user.username,
        email=new_user.email,
        password=new_user.password
    )
    user_repository.insert_user(user)

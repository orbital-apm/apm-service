# Importing necessary packages for authentication-related services
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.db.models.models import User
from app.api.models.auth_models import RegistrationRequest


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bool(pwd_context.verify(plain_password, hashed_password))


def get_password_hash(password: str) -> str:
    return str(pwd_context.hash(password))


def get_user(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


def authenticate_user(db: Session, username: str, password: str): # type: ignore
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, str(user.hashed_password)):
        return False
    return user


def create_user(db: Session, user: RegistrationRequest) -> User:
    hashed_password = get_password_hash(RegistrationRequest.password)
    db_user = User(username=RegistrationRequest.username, email=RegistrationRequest.email,
                   hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Loading the necessary packages
import jwt
import os

from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidTokenError
from dotenv import load_dotenv
from typing import Annotated

from app.api.models.auth_models import Token, TokenData, User, RegistrationRequest
from app.services.security import authenticate_user, create_user
from app.db.database import get_db

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:  # type: ignore
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"},)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = db.query(User).filter(User.username == token_data.username).first()  # type: ignore
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)],) -> User:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user.")
    return current_user


@router.post("/login")
def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                       db: Session = Depends(get_db)) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401,
                            detail="Incorrect username or password.",
                            headers={"WWW-Authenticate": "Bearer"})
    elif user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user. Please register again.")
    access_expiry = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username},
                                       expires_delta=access_expiry)
    return Token(access_token=access_token, token_type="bearer")


@router.post("/register")
def register_user(user: RegistrationRequest, db: Session = Depends(get_db)) -> User:
    db_user = db.query(User).filter(User.email == user.email).first()  # type: ignore
    if db_user:
        raise HTTPException(status_code=400,
                            detail="This email is already in use.")
    elif RegistrationRequest.confirm_password != RegistrationRequest.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Passwords do not match.")
    return create_user(db=db, user=user)


@router.get("/users/me/")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]) -> User:
    return current_user

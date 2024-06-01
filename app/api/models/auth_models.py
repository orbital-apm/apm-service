from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: EmailStr | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


class LoginRequest(BaseModel):
    email: EmailStr
    username: str | None
    password: str


class RegistrationRequest(BaseModel):
    email: EmailStr
    username: str | None
    password: str
    confirm_password: str

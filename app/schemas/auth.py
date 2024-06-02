from pydantic import BaseModel, EmailStr


class LoginUserSchema(BaseModel):  # type: ignore[misc]
    email: EmailStr
    password: str


class RegisterUserSchema(BaseModel):  # type: ignore[misc]
    email: EmailStr
    username: str
    password: str

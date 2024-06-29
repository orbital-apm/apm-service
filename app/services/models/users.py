from pydantic import BaseModel, EmailStr


class AddUserParams(BaseModel):  # type: ignore[misc]
    email: EmailStr
    username: str
    password: str


class User(BaseModel):  # type: ignore[misc]
    id: str
    email: str
    username: str
    password: str

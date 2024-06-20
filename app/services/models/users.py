from pydantic import BaseModel, EmailStr


class AddUserParams(BaseModel):  # type: ignore[misc]
    email: EmailStr
    username: str
    password: str

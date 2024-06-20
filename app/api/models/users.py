from pydantic import BaseModel, EmailStr


class AddUserRequest(BaseModel):  # type: ignore[misc]
    email: EmailStr
    username: str
    password: str

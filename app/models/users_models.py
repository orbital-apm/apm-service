from pydantic import BaseModel, EmailStr


class UserAddRequest(BaseModel):  # type: ignore[misc]
    email: EmailStr
    username: str
    password: str

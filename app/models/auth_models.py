from pydantic import BaseModel, EmailStr


class TokenRequest(BaseModel):  # type: ignore[misc]
    email: EmailStr
    password: str

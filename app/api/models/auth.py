from pydantic import BaseModel, EmailStr


class GenerateTokenRequest(BaseModel):  # type: ignore[misc]
    email: EmailStr
    password: str

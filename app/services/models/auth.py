from pydantic import BaseModel, EmailStr


class GenerateTokenParams(BaseModel):  # type: ignore[misc]
    email: EmailStr
    password: str

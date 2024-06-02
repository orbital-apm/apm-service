from pydantic import BaseModel, EmailStr


class NewUserSchema(BaseModel):  # type: ignore[misc]
    email: EmailStr
    username: str
    password: str

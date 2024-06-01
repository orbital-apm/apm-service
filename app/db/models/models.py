from sqlalchemy import Column, Integer, String
from app.db.database import Base


class User(Base):  # type: ignore
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # is_active = Column(Boolean, default = True)//Users/phone_mon/Downloads/Orbital 2024 /apm-service/app

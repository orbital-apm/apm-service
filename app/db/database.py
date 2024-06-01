import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("DATABASE_POSTGRE_URL")

engine = create_engine(str(url))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():  # type: ignore
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

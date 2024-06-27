import os
from typing import Generator

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.db.database import Base

load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def clear_database() -> Generator[None, None, None]:
    db_name = os.getenv("DB_NAME")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_username = os.getenv("DB_USERNAME")
    db_password = os.getenv("DB_PASSWORD")
    engine = create_engine(f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

    Base.metadata.drop_all(bind=engine)  # type: ignore[attr-defined]
    Base.metadata.create_all(bind=engine)  # type: ignore[attr-defined]

    yield

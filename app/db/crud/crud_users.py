from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import cast
from app.db.models.user import UserEntity


def get_user_name(db: Session, user_id: UUID) -> str:
    query = select(UserEntity).where(UserEntity.id == user_id)
    result = db.execute(query)
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")

    return cast(UserEntity, user).username


def get_user_email(db: Session, user_id: UUID) -> str:
    query = select(UserEntity).where(UserEntity.id == user_id)
    result = db.execute(query)
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")

    return cast(UserEntity, user).email

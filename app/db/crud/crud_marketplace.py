from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import cast
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from app.db.models.marketplace import Listings
from app.schemas.marketplace_schemas.marketplace_schemas import ListingsSchema


def get_listings(db: Session) -> Page[ListingsSchema]:
    query = select(Listings)
    result: Page[ListingsSchema] = paginate(db, query)
    return result


def get_listing(db: Session, uuid: UUID) -> Listings:
    query = select(Listings).where(Listings.id == uuid)
    result = db.execute(query)
    listing = result.scalar_one_or_none

    if listing is None:
        raise HTTPException(status_code=404, detail="Information not found.")

    return cast(Listings, listing)


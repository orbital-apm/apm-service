from fastapi import Depends, HTTPException, APIRouter, status, Header
from sqlalchemy.orm import Session
from uuid import UUID
from fastapi_pagination import Page, add_pagination
from fastapi.responses import JSONResponse
from typing import Annotated

from app.db.crud import crud_marketplace
from app.db.database import get_db
from app.api.models.listings import GenerateListing, ListingsResponse
from app.api.deps import get_current_user_id
from app.schemas.marketplace_schemas import ListingsSchema
from app.services.listings_service import create_listing

router = APIRouter()


@router.get('/listings', response_model=Page[ListingsSchema])
def marketplace(db: Session = Depends(get_db)) -> Page[ListingsSchema]:
    try:
        return crud_marketplace.get_listings(db)
    except Exception:
        raise Exception


@router.get('/listings/{id}')
def get_listing(id: UUID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        return crud_marketplace.get_listing(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post('/listings', response_model=ListingsResponse, status_code=status.HTTP_201_CREATED)
def listing_route(request: GenerateListing, authorization: Annotated[str | None, Header()],
                  db: Session = Depends(get_db)) -> JSONResponse:
    try:
        user_id = get_current_user_id(authorization)
        listing = create_listing(db, request, UUID(user_id))
        return listing
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


add_pagination(router)

from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.orm import Session
from uuid import UUID
from fastapi_pagination import Page, add_pagination
from fastapi.responses import JSONResponse

from app.db.crud import crud_marketplace
from app.db.database import get_db
from app.db.models.user import UserEntity
from app.api.models.listings import GenerateListing, ListingsResponse
from app.api.deps import get_current_user
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
def listing_route(request: GenerateListing, current_user: UserEntity = Depends(get_current_user), 
                  db: Session = Depends(get_db)) -> JSONResponse:
    try:
        if get_current_user is not None:
            listing = create_listing(db, request, UUID(current_user.id))
            return listing
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


add_pagination(router)

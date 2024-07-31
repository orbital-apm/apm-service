from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.database import get_db
from app.api.models.users import AddUserRequest
from app.services.users_service import add_user
from app.services.models.users import AddUserParams
from app.db.crud.crud_users import get_user_name, get_user_email

router = APIRouter(prefix="/users")


@router.post(path="")
def add_user_route(request: AddUserRequest, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        access_token = add_user(AddUserParams(**request.model_dump()), db)

        response_payload = {
            "access_token": access_token,
            "token_type": "bearer"
        }

        return JSONResponse(response_payload, status_code=201)

    except HTTPException:
        raise

    except Exception:
        # Todo: Handle exceptions.
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get('/{id}/username')
def get_name(id: UUID, db: Session = Depends(get_db)) -> str:
    try:
        return get_user_name(db, id)
    except Exception:
        raise


@router.get('/{id}/email')
def get_email(id: UUID, db: Session = Depends(get_db)) -> str:
    try:
        return get_user_email(db, id)
    except Exception:
        raise

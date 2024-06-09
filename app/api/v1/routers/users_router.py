from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.users_models import UserAddRequest
from app.services.users_service import add_user

router = APIRouter(prefix="/users")


@router.post(path="")
def add_user_route(user: UserAddRequest, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        add_user(user, db)

        # Todo: Return token.
        return JSONResponse({}, status_code=201)

    except HTTPException:
        raise

    except Exception:
        # Todo: Handle exceptions.
        raise HTTPException(status_code=500, detail="Internal Server Error")

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.api.models.users import AddUserRequest
from app.services.users_service import add_user
from app.services.models.users import AddUserParams

router = APIRouter(prefix="/users")


@router.post(path="")
def add_user_route(request: AddUserRequest, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        add_user(AddUserParams(**request.model_dump()), db)

        # Todo: Return token.
        return JSONResponse({}, status_code=201)

    except HTTPException:
        raise

    except Exception:
        # Todo: Handle exceptions.
        raise HTTPException(status_code=500, detail="Internal Server Error")

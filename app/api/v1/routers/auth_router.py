from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.auth_models import TokenRequest
from app.services.auth_service import get_token

router = APIRouter(prefix="/auth")


@router.post("/token")
def token_route(user: TokenRequest, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        # Todo: Refresh token.
        access_token = get_token(user, db)

        response_payload = {
            "access_token": access_token,
            "token_type": "bearer"
        }

        return JSONResponse(response_payload, status_code=200)

    except HTTPException:
        raise

    except Exception:
        # Todo: Handle exceptions.
        raise HTTPException(status_code=500, detail="Internal Server Error")

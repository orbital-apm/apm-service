from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.api.models.auth import GenerateTokenRequest
from app.services.auth_service import get_token
from app.services.models.auth import GenerateTokenParams

router = APIRouter(prefix="/auth")


@router.post("/token")
def token_route(request: GenerateTokenRequest, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        # Todo: Refresh token.
        access_token = get_token(GenerateTokenParams(**request.model_dump()), db)

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

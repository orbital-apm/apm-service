from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import insert
from uuid import UUID, uuid4

from app.db.database import get_db
from app.api.models.builds import GenerateBuild
from app.db import crud
from app.db.models.builder import Builds


router = APIRouter()


@router.get("/builds/{id}")
async def build(id: UUID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        return crud.get_build(db, uuid=id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/builds")
def create_build(build: GenerateBuild, db: Session = Depends(get_db)) -> UUID:
    build_id = uuid4()

    query = insert(Builds).values(
        id=build_id,
        build_name=build.build_name,
        switch_id=build.switch_id,
        kit_id=build.kit_id,
        keycap_id=build.keycap_id,
        lubricant_id=build.lubricant_id
    )

    try:
        db.execute(query)
        db.commit()

    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to create build: {str(Exception)}")

    return build_id

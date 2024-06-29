from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
# import uuid

from app.db.database import get_db
from app.db import crud
# from app.schemas.build import _
# To do: Set up schemas for builder


router = APIRouter()


@router.get("/products/keycaps")
def get_keycaps(db: Session = Depends(get_db)):
    try:
        return crud.get_keycaps(db)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/switches")
def get_switches(db: Session = Depends(get_db)):
    try:
        return crud.get_switches(db)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/kits")
def get_kits(db: Session = Depends(get_db)):
    try:
        return crud.get_kits(db)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/lubricants")
def get_lubricants(db: Session = Depends(get_db)):
    try:
        return crud.get_lubricants(db)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


# @router.get("/products/keycaps/{id}")
# async def keycap(uuid: uuid, db: Session = Depends(get_db)):
#    return

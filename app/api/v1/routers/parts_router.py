from fastapi import Depends, HTTPException, APIRouter, Query
from fastapi_pagination import Page, add_pagination, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID

from app.db.database import get_db
from app.db import crud
from app.db.models.builder import Keycap, Switch, Kits, Lubricant
from app.schemas.parts import KeycapOut, SwitchOut, KitsOut, LubricantsOut

# from app.schemas.build import _
# To do: Set up schemas for builder


router = APIRouter()


@router.get("/products/keycaps", response_model=Page[KeycapOut])
def get_keycaps(db: Session = Depends(get_db)):
    try:
        query = select(Keycap)
        return paginate(db, query)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/keycaps/{id}")
async def keycap(id: UUID, db: Session = Depends(get_db)):
    try:
        return crud.get_keycap(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/switches", response_model=Page[SwitchOut])
def get_switches(db: Session = Depends(get_db)):
    try:
        query = select(Switch)
        return paginate(db, query)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/switches/{id}")
async def switch(id: UUID, db: Session = Depends(get_db)):
    try:
        return crud.get_switch(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/kits", response_model=Page[KitsOut])
def get_kits(db: Session = Depends(get_db)):
    try:
        query = select(Kits)
        return paginate(db, query)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/kits/{id}")
async def kit(id: UUID, db: Session = Depends(get_db)):
    try:
        return crud.get_kit(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/lubricants", response_model=Page[LubricantsOut])
def get_lubricants(db: Session = Depends(get_db)):
    try:
        query = select(Lubricant)
        return paginate(db, query)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/lubricants/{id}")
async def lubricant(id: UUID, db: Session = Depends(get_db)):
    try:
        return crud.get_lubricant(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


add_pagination(router)
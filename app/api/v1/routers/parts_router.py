from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID

from app.db.database import get_db
from app.db import crud
from app.db.models.builder import Keycap, Switch, Kits, Lubricant
from app.schemas.parts import KeycapOut, SwitchOut, KitsOut, LubricantsOut


router = APIRouter()


@router.get("/parts/keycaps", response_model=Page[KeycapOut])
def get_keycaps(db: Session = Depends(get_db)) -> Page[KeycapOut]:
    try:
        query = select(Keycap)
        result: Page[KeycapOut] = paginate(db, query)
        return result
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/keycaps/{id}")
async def keycap(id: UUID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        return crud.get_keycap(db, id)
    except Exception:
        raise Exception


@router.get("/parts/switches", response_model=Page[SwitchOut])
def get_switches(db: Session = Depends(get_db)) -> Page[SwitchOut]:
    try:
        query = select(Switch)
        result: Page[SwitchOut] = paginate(db, query)
        return result
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/switches/{id}")
async def switch(id: UUID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        return crud.get_switch(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/kits", response_model=Page[KitsOut])
def get_kits(db: Session = Depends(get_db)) -> Page[KitsOut]:
    try:
        query = select(Kits)
        result: Page[KitsOut] = paginate(db, query)
        return result
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/kits/{id}")
async def kit(id: UUID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        return crud.get_kit(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/lubricants", response_model=Page[LubricantsOut])
def get_lubricants(db: Session = Depends(get_db)) -> Page[LubricantsOut]:
    try:
        query = select(Lubricant)
        result: Page[LubricantsOut] = paginate(db, query)
        return result
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/products/lubricants/{id}")
async def lubricant(id: UUID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        return crud.get_lubricant(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


add_pagination(router)

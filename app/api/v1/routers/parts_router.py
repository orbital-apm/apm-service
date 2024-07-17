from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID

from app.db.database import get_db
from app.db import crud
from app.db.models.builder import Keycap, Switch, Kits, Lubricant
from app.schemas.parts_schemas.parts import KeycapSchema, SwitchSchema, KitsSchema, LubricantsSchema
from app.schemas.parts_schemas.parts_filters import KeycapFilter, SwitchFilter, KitsFilter


router = APIRouter()


@router.get("/parts/keycaps", response_model=Page[KeycapSchema])
def get_keycaps(db: Session = Depends(get_db),
                keycap_filter: KeycapFilter = FilterDepends(KeycapFilter)) -> Page[KeycapSchema]:
    try:
        query = select(Keycap)
        query = keycap_filter.filter(query)
        query = keycap_filter.sort(query)
        result: Page[KeycapSchema] = paginate(db, query)
        return result
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/keycaps/{id}")
async def keycap(id: UUID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        return crud.get_keycap(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/switches", response_model=Page[SwitchSchema])
def get_switches(db: Session = Depends(get_db),
                 switch_filter: SwitchFilter = FilterDepends(SwitchFilter)) -> Page[SwitchSchema]:
    try:
        query = select(Switch)
        query = switch_filter.filter(query)
        result: Page[SwitchSchema] = paginate(db, query)
        return result
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/switches/{id}")
async def switch(id: UUID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        return crud.get_switch(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/kits", response_model=Page[KitsSchema])
def get_kits(db: Session = Depends(get_db),
             kits_filter: KitsFilter = FilterDepends(KitsFilter)) -> Page[KitsSchema]:
    try:
        query = select(Kits)
        query = kits_filter.filter(query)
        result: Page[KitsSchema] = paginate(db, query)
        return result
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/kits/{id}")
async def kit(id: UUID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        return crud.get_kit(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/lubricants", response_model=Page[LubricantsSchema])
def get_lubricants(db: Session = Depends(get_db)) -> Page[LubricantsSchema]:
    try:
        query = select(Lubricant)
        result: Page[LubricantsSchema] = paginate(db, query)
        return result
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/parts/lubricants/{id}")
async def lubricant(id: UUID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        return crud.get_lubricant(db, id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


add_pagination(router)

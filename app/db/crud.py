from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.db.models.builder import Keycap, Switch, Lubricant, Kits, Builds


# Functions for parts listings page:


def get_keycaps(db: Session) -> list[Keycap]:
    return db.query(Keycap).all()


def get_switches(db: Session) -> list[Switch]:
    return db.query(Switch).all()


def get_lubricants(db: Session) -> list[Lubricant]:
    return db.query(Lubricant).all()


def get_kits(db: Session) -> list[Kits]:
    return db.query(Kits).all()


def get_builds(db: Session) -> list[Builds]:
    return db.query(Builds).all()

# Functions for specific parts listing page


def get_keycap(db: Session, uuid: UUID) -> JSONResponse:
    query = select(Keycap).where(Keycap.id == uuid)
    result = db.execute(query)
    keycap = result.scalar_one_or_none()

    if keycap is None:
        raise HTTPException(status_code=404, detail="Information not found.")

    return JSONResponse(content=jsonable_encoder(keycap))


def get_switch(db: Session, uuid: UUID) -> JSONResponse:
    query = select(Switch).where(Switch.id == uuid)
    result = db.execute(query)
    switch = result.scalar_one_or_none()

    if switch is None:
        raise HTTPException(status_code=404, detail="Information not found")

    return JSONResponse(content=jsonable_encoder(switch))


def get_kit(db: Session, uuid: UUID) -> JSONResponse:
    query = select(Kits).where(Kits.id == uuid)
    result = db.execute(query)
    kits = result.scalar_one_or_none()

    if kits is None:
        raise HTTPException(status_code=404, detail="Information not found")

    return JSONResponse(content=jsonable_encoder(kits))


def get_lubricant(db: Session, uuid: UUID) -> JSONResponse:
    query = select(Lubricant).where(Lubricant.id == uuid)
    result = db.execute(query)
    lubricant = result.scalar_one_or_none()

    if lubricant is None:
        raise HTTPException(status_code=404, detail="Information not found")

    return JSONResponse(content=jsonable_encoder(lubricant))


def get_build(db: Session, uuid: UUID) -> JSONResponse:
    query = select(Builds).where(Builds.id == uuid)
    result = db.execute(query)
    build = result.scalar_one_or_none()

    if build is None:
        raise HTTPException(status_code=404, detail="Information not found")

    return JSONResponse(content=jsonable_encoder(build))

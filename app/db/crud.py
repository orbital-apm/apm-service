from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models.builder import Keycap, Switch, Lubricant, Kits, Builds
import typing


def get_keycaps(db: Session) -> list[typing.Any]:  # type: ignore
    return db.query(Keycap).all()


def get_switches(db: Session) -> list[typing.Any]:  # type: ignore
    return db.query(Switch).all()


def get_lubricants(db: Session) -> list[typing.Any]:  # type: ignore
    return db.query(Lubricant).all()


def get_kits(db: Session) -> list[typing.Any]:  # type: ignore
    return db.query(Kits).all()


def get_builds(db: Session) -> list[typing.Any]:  # type: ignore
    return db.query(Builds).all()


# To do: Check whether the function has the correct logic.

def keycap_info(db: Session, uuid: UUID):  # type: ignore
    query = select(Keycap).where(Keycap.id == uuid)
    result = db.execute(query)
    keycap = result.scalar_one_or_none()

    if keycap is None:
        raise HTTPException(status_code=404, detail="Information not found.")

    return keycap


def switch_info(db: Session, uuid: UUID):  # type: ignore
    query = select(Switch).where(Switch.id == uuid)
    result = db.execute(query)
    switch = result.scalar_one_or_none()

    if switch is None:
        raise HTTPException(status_code=404, detail="Information not found")

    return switch


def kit_info(db: Session, uuid: UUID):  # type: ignore
    query = select(Kits).where(Kits.id == uuid)
    result = db.execute(query)
    kits = result.scalar_one_or_none()

    if kits is None:
        raise HTTPException(status_code=404, detail="Information not found")

    return kits


def lubricant_info(db: Session, uuid: UUID):  # type: ignore
    query = select(Lubricant).where(Lubricant.id == uuid)
    result = db.execute(query)
    lubricant = result.scalar_one_or_none()

    if lubricant is None:
        raise HTTPException(status_code=404, detail="Information not found")

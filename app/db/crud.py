from sqlalchemy.orm import Session
from models.builder import Keycap, Switch, Lubricant, Kits


def get_keycaps(db: Session):
    return db.query(Keycap).all()

def get_switches(db: Session):
    return db.query(Switch).all()

def get_lubricants(db: Session):
    return db.query(Lubricant).all()

def get_kits(db: Session):
    return db.query(Kits).all()



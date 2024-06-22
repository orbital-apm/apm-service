import uuid
from sqlalchemy import ARRAY, String
from sqlalchemy.orm import Mapped, mapped_column  # type: ignore[attr-defined]
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base


# Keyboard Switches Table


class Switch(Base):  # type: ignore
    __tablename__ = "switches"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    price: Mapped[float] = mapped_column(unique=False, nullable=True)
    manufacturer: Mapped[str] = mapped_column(unique=False, nullable=True)
    switch_type: Mapped[str] = mapped_column(unique=False, nullable=False)
    actuation_force: Mapped[float] = mapped_column(unique=False, nullable=True)
    travel_distance: Mapped[float] = mapped_column(unique=False, nullable=True)
    vendor: Mapped[list[str]] = mapped_column(ARRAY(String), unique=False, nullable=True)
    img_url: Mapped[str] = mapped_column(unique=False, nullable=True)


# Keyboard Keycaps Table


class Keycap(Base):  # type: ignore
    __tablename__ = "keycaps"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    price: Mapped[float] = mapped_column(unique=False, nullable=True)
    manufacturer: Mapped[str] = mapped_column(unique=False, nullable=True)
    vendor: Mapped[list[str]] = mapped_column(ARRAY(String), unique=False, nullable=True)
    colors: Mapped[list[str]] = mapped_column(ARRAY(String), unique=False, nullable=True)
    layout: Mapped[list[str]] = mapped_column(ARRAY(String), unique=False, nullable=True)
    material: Mapped[str] = mapped_column(unique=False, nullable=True)
    profile: Mapped[str] = mapped_column(unique=False, nullable=True)
    img_url: Mapped[str] = mapped_column(unique=False, nullable=True)


# Keyboard Lubricants Table


class Lubricant(Base):  # type: ignore
    __tablename__ = "lubricants"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    price: Mapped[float] = mapped_column(unique=False, nullable=True)
    brand: Mapped[str] = mapped_column(unique=False, nullable=True)
    img_url: Mapped[str] = mapped_column(unique=False, nullable=True)

# Keyboard Kits Table
    

class Kits(Base): # type: ignore
    __tablename__ = "kits"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    manufacturer: Mapped[str] = mapped_column(unique=False, nullable=True)

    layout_size: Mapped[int] = mapped_column(unique=False, nullable=False)
    layout_standard: Mapped[str] = mapped_column(unique=False, nullable=True)
    layout_ergonomic: Mapped[str] = mapped_column(unique=False, nullable=True)

    hotswappable: Mapped[bool] = mapped_column(unique=False, nullable=True)
    knob_support: Mapped[bool] = mapped_column(unique=False, nullable=True)
    rgb_support: Mapped[bool] = mapped_column(unique=False, nullable=True)
    display_support: Mapped[bool] = mapped_column(unique=False, nullable=True)

    connection: Mapped[str] = mapped_column(unique=False, nullable=True)
    mount_style: Mapped[str] = mapped_column(unique=False, nullable=True)
    material: Mapped[str] = mapped_column(unique=False, nullable=True)

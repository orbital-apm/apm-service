import uuid
from sqlalchemy.orm import Mapped, mapped_column  # type: ignore[attr-defined]
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base


# Keyboard Switches Table


class Switch(Base):  # type: ignore
    __tablename__ = "switches"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    price_per_unit: Mapped[float] = mapped_column(unique=False, nullable=True)
    manufacturer: Mapped[str] = mapped_column(unique=False, nullable=True)
    actuation_force: Mapped[float] = mapped_column(unique=False, nullable=True)
    travel_distance: Mapped[float] = mapped_column(unique=False, nullable=True)
    vendor: Mapped[str] = mapped_column(unique=False, nullable=True)


# Keyboard Keycaps Table


class Keycap(Base):  # type: ignore
    __tablename__ = "keycaps"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    price: Mapped[float] = mapped_column(unique=False, nullable=True)
    brand: Mapped[str] = mapped_column(unique=False, nullable=True)
    vendor: Mapped[str] = mapped_column(unique=False, nullable=True)
    sub_legends: Mapped[str] = mapped_column(unique=False, nullable=False)
    material: Mapped[str] = mapped_column(unique=False, nullable=False)
    profile: Mapped[str] = mapped_column(unique=False, nullable=False)


# Keyboard Lubricants Table


class Lubricant(Base):  # type: ignore
    __tablename__ = "lubricants"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    price: Mapped[float] = mapped_column(unique=False, nullable=True)
    brand: Mapped[str] = mapped_column(unique=False, nullable=True)


# Keyboard Kits Table

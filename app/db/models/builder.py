import uuid
from sqlalchemy import ARRAY, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column  # type: ignore[attr-defined]
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base

# Keyboard Switches Table


class Switch(Base):  # type: ignore
    __tablename__ = "switches"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    price: Mapped[float] = mapped_column(unique=False, nullable=True)
    manufacturer: Mapped[str] = mapped_column(unique=False, nullable=True)
    switch_type: Mapped[str] = mapped_column(unique=False, nullable=False)
    actuation_force: Mapped[str] = mapped_column(unique=False, nullable=True)
    travel_distance: Mapped[str] = mapped_column(unique=False, nullable=True)
    vendor: Mapped[list[str]] = mapped_column(ARRAY(String), unique=False, nullable=True)
    img_url: Mapped[str] = mapped_column(unique=False, nullable=True)
    availability: Mapped[str] = mapped_column(unique=False, nullable=True)


# Keyboard Keycaps Table


class Keycap(Base):  # type: ignore
    __tablename__ = "keycaps"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    price: Mapped[float] = mapped_column(unique=False, nullable=True)
    manufacturer: Mapped[str] = mapped_column(unique=False, nullable=True)
    vendor: Mapped[list[str]] = mapped_column(ARRAY(String), unique=False, nullable=True)
    colors: Mapped[list[str]] = mapped_column(ARRAY(String), unique=False, nullable=True)
    layout: Mapped[list[str]] = mapped_column(ARRAY(String), unique=False, nullable=True)
    material: Mapped[str] = mapped_column(unique=False, nullable=True)
    profile: Mapped[str] = mapped_column(unique=False, nullable=True)
    img_url: Mapped[str] = mapped_column(unique=False, nullable=True)
    availability: Mapped[bool] = mapped_column(unique=False, nullable=True)

# Keyboard Lubricants Table


class Lubricant(Base):  # type: ignore
    __tablename__ = "lubricants"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    price: Mapped[str] = mapped_column(unique=False, nullable=True)
    img_url: Mapped[str] = mapped_column(unique=False, nullable=True)
    availability: Mapped[bool] = mapped_column(unique=False, nullable=True)

# Keyboard Kits Table


class Kits(Base):  # type: ignore
    __tablename__ = "kits"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    price: Mapped[float] = mapped_column(unique=False, nullable=True)
    manufacturer: Mapped[str] = mapped_column(unique=False, nullable=True)
    vendor: Mapped[list[str]] = mapped_column(ARRAY(String), unique=False, nullable=True)

    layout_size: Mapped[str] = mapped_column(unique=False, nullable=False)
    layout_standard: Mapped[str] = mapped_column(unique=False, nullable=True)
    layout_ergonomic: Mapped[str] = mapped_column(unique=False, nullable=True)

    hotswappable: Mapped[bool] = mapped_column(unique=False, nullable=True)
    knob_support: Mapped[bool] = mapped_column(unique=False, nullable=True)
    rgb_support: Mapped[bool] = mapped_column(unique=False, nullable=True)
    display_support: Mapped[bool] = mapped_column(unique=False, nullable=True)

    connection: Mapped[list[str]] = mapped_column(ARRAY(String), unique=False, nullable=True)
    mount_style: Mapped[str] = mapped_column(unique=False, nullable=True)
    material: Mapped[str] = mapped_column(unique=False, nullable=True)
    img_url: Mapped[str] = mapped_column(unique=False, nullable=True)
    availability: Mapped[bool] = mapped_column(unique=False, nullable=True)


class Builds(Base):  # type: ignore
    __tablename__ = "builds"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    build_name: Mapped[str] = mapped_column(unique=False, nullable=True)
#   user_id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    kit_id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey("kits.id"), default=uuid.uuid4)
    switch_id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey("switches.id"), default=uuid.uuid4)
    keycap_id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey("keycaps.id"), default=uuid.uuid4)
    lubricant_id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey("lubricants.id"), default=uuid.uuid4)

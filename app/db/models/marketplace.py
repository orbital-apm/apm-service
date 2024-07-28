import uuid
from sqlalchemy import ARRAY, ForeignKey, VARCHAR, Numeric
from sqlalchemy.orm import Mapped, mapped_column  # type: ignore[attr-defined]
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.database import Base


class Listings(Base):  # type: ignore
    __tablename__ = "listings"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    title: Mapped[str] = mapped_column(unique=False, nullable=True)
    description: Mapped[str] = mapped_column(unique=False, nullable=True)
    condition: Mapped[int] = mapped_column(unique=False, nullable=True)
    part_type: Mapped[list[str]] = mapped_column(ARRAY(VARCHAR), unique=False, nullable=True)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    price: Mapped[Numeric] = mapped_column(Numeric(10, 2), unique=False, nullable=True)

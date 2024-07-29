from sqlalchemy.orm import Session
from uuid import UUID, uuid4

from app.api.models.listings import GenerateListing
from app.db.models.marketplace import Listings


def create_listing(db: Session, listing: GenerateListing, user_id: UUID = uuid4()) -> Listings:
    try:
        new_listing = Listings(
            title=listing.title,
            description=listing.description,
            condition=listing.condition,
            part_type=listing.part_type,
            price=listing.price,
            user_id=user_id
        )
        db.add(new_listing)
        db.commit()
        db.refresh(new_listing)
        return new_listing
    except Exception:
        raise

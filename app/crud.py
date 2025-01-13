from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models import Location, Category, LocationCategoryReviewed
from sqlalchemy import or_, asc, desc

def create_location(db: Session, latitude: float, longitude: float):
    new_location = Location(latitude=latitude, longitude=longitude)
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location

def create_category(db: Session, name: str):
    new_category = Category(name=name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def create_location_category_reviewed(db: Session, location_id: int, category_id: int):
    new_review = LocationCategoryReviewed(
        location_id=location_id,
        category_id=category_id,
        reviewed_at=datetime.utcnow(),
        is_reviewed=False
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

def update_review(db: Session, review_id: int):
    review = db.query(LocationCategoryReviewed).filter_by(id=review_id).first()
    if not review:
        return None
    review.reviewed_at = datetime.utcnow()
    review.is_reviewed = True
    db.commit()
    db.refresh(review)
    return review

def get_explore_recommendations(db: Session, days_ago: int = 30, limit: int = 10):
    thirty_days_ago = datetime.utcnow() - timedelta(days=days_ago)
    return (
        db.query(LocationCategoryReviewed)
        .join(Location, Location.id == LocationCategoryReviewed.location_id)
        .join(Category, Category.id == LocationCategoryReviewed.category_id)
        .filter(
            or_(
                LocationCategoryReviewed.reviewed_at.is_(None),
                LocationCategoryReviewed.reviewed_at < thirty_days_ago,
            )
        )
        .order_by(
            asc(LocationCategoryReviewed.reviewed_at.isnot(None)),
            desc(LocationCategoryReviewed.reviewed_at)
        )
        .limit(limit)
        .all()
    )

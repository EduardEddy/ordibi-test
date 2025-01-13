from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import LocationCategoryReviewedCreate
from app.crud import create_location_category_reviewed, update_review
from app.models import LocationCategoryReviewed

router = APIRouter()

@router.post("/")
def create(locationCategory: LocationCategoryReviewedCreate, db: Session = Depends(get_db)):
    return create_location_category_reviewed(db, location_id=locationCategory.location_id, category_id=locationCategory.category_id)

@router.put("/{review_id}")
def review_location(review_id: int, db: Session = Depends(get_db)):
    return update_review(db, review_id)
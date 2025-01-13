from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import LocationCreate
from app.crud import create_location
from app.models import Location

router = APIRouter()

@router.post("/")
def create(location: LocationCreate, db: Session = Depends(get_db)):
    return create_location(db, latitude=location.latitude, longitude=location.longitude)

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(Location).all()

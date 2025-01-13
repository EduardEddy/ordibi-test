from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
#from app.schemas import LocationCreate
from app.crud import get_explore_recommendations
#from app.models import Location

router = APIRouter()

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return get_explore_recommendations(db)

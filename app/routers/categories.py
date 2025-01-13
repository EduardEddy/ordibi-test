from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import CategoryCreate
from app.crud import create_category
from app.models import Category

router = APIRouter()

@router.post("/")
def create(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, name=category.name)

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(Category).all()
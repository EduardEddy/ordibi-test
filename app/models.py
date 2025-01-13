from sqlalchemy import (
    Column, Integer, String, Float, ForeignKey, DateTime, Boolean, UniqueConstraint
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import as_declarative
from datetime import datetime

@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Location(Base):
    __tablename__ = 'locations'
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

class Category(Base):
    __tablename__ = 'categories'
    name = Column(String(255), nullable=False, unique=True)

class LocationCategoryReviewed(Base):
    __tablename__ = 'location_category_reviewed'
    id = Column(Integer, primary_key=True, index=True)  # Nuevo campo
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    reviewed_at = Column(DateTime, nullable=True)
    is_reviewed = Column(Boolean, default=False, nullable=False)

    location = relationship('Location')
    category = relationship('Category')

    # Restringir combinaciones duplicadas de ubicación y categoría
    __table_args__ = (
        UniqueConstraint('location_id', 'category_id', name='unique_location_category'),
    )

from pydantic import BaseModel

class LocationCreate(BaseModel):
    latitude: float
    longitude: float

class CategoryCreate(BaseModel):
    name: str

class LocationCategoryReviewedCreate(BaseModel):
    location_id: int
    category_id: int

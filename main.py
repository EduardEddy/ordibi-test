from fastapi import FastAPI
from app.routers import locations, categories, reviews, recommendations

app = FastAPI()

app.include_router(locations.router, prefix="/locations", tags=["Locations"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
app.include_router(recommendations.router, prefix="/explore_recommendations", tags=["Recommendations"])

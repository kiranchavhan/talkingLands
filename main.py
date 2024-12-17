import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

# File: main.py
from fastapi import FastAPI
from database import init_db
from src.routers import point_routes, polygon_routes

# FastAPI app
app = FastAPI()

# Initialize database
@app.on_event("startup")
def startup_event():
    init_db()

# Include Routers
app.include_router(point_routes.router, prefix="/points", tags=["Points"])
app.include_router(polygon_routes.router, prefix="/polygons", tags=["Polygons"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
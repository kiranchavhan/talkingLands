# File: routers/polygon_routes.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models import PolygonModel
from src.schemas import Polygon
from database import get_db

router = APIRouter()

def polygon_to_wkt(coordinates: List[List[float]]) -> str:
    points = ", ".join([f"{lon} {lat}" for lon, lat in coordinates])
    return f"POLYGON(({points}))"

@router.post("/", response_model=Polygon)
def create_polygon(polygon: Polygon, db: Session = Depends(get_db)):
    polygon_wkt = polygon_to_wkt(polygon.coordinates)
    db_polygon = PolygonModel(name=polygon.name, coordinates=f"SRID=4326;{polygon_wkt}")
    db.add(db_polygon)
    db.commit()
    db.refresh(db_polygon)
    return db_polygon

@router.get("/{polygon_id}", response_model=Polygon)
def get_polygon(polygon_id: int, db: Session = Depends(get_db)):
    db_polygon = db.query(PolygonModel).filter(PolygonModel.id == polygon_id).first()
    if not db_polygon:
        raise HTTPException(status_code=404, detail="Polygon not found")
    return db_polygon

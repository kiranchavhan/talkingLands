from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models import PointModel
from src.schemas import Point
from database import get_db

router = APIRouter()

@router.post("/", response_model=Point)
def create_point(point: Point, db: Session = Depends(get_db)):
    db_point = PointModel(name=point.name, coordinates=f"SRID=4326;POINT({point.coordinates[0]} {point.coordinates[1]})")
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point

@router.get("/{point_id}", response_model=Point)
def get_point(point_id: int, db: Session = Depends(get_db)):
    db_point = db.query(PointModel).filter(PointModel.id == point_id).first()
    if not db_point:
        raise HTTPException(status_code=404, detail="Point not found")
    return db_point
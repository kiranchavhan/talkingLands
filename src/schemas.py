from pydantic import BaseModel
from typing import List

class Point(BaseModel):
    id: int
    name: str
    coordinates: List[float]  # [longitude, latitude]

    class Config:
        orm_mode = True

class Polygon(BaseModel):
    id: int
    name: str
    coordinates: List[List[float]]  # List of [longitude, latitude] pairs

    class Config:
        orm_mode = True
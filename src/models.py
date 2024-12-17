from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geography
from database import Base

class PointModel(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    coordinates = Column(Geography(geometry_type="POINT", srid=4326), nullable=False)

class PolygonModel(Base):
    __tablename__ = "polygons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    coordinates = Column(Geography(geometry_type="POLYGON", srid=4326), nullable=False)
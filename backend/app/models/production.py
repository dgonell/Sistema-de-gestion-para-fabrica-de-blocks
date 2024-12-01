from sqlalchemy import Column, Integer, String, Date, Numeric
from app.database import Base

class Production(Base):
    __tablename__ = "produccion"

    id = Column(Integer, primary_key=True, index=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    paletas = Column(Integer, nullable=False)
    blocks = Column(Integer, nullable=False)
    costo_total = Column(Numeric(10, 2), nullable=False)

from sqlalchemy import Column, Integer, String
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    cedula_rnc = Column(String(13), unique=True, nullable=False)
    telefono = Column(String(15), nullable=False)
    direccion = Column(String(255), nullable=True)



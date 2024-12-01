from pydantic import BaseModel,Field
from datetime import date

class ClienteBase(BaseModel):
    nombre: str
    cedula_rnc: str
    telefono: str
    direccion: str | None = None

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: int

    class Config:
        orm_mode = True
# Base Schema para Producción
class ProductionBase(BaseModel):
    fecha_inicio: date = Field(..., title="Fecha de Inicio", example="2024-11-01")
    fecha_fin: date = Field(..., title="Fecha de Fin", example="2024-11-02")
    paletas: int = Field(..., gt=0, title="Cantidad de Paletas", example=10)
    blocks: int = Field(..., gt=0, title="Cantidad de Blocks", example=1000)
    costo_total: float = Field(..., gt=0, title="Costo Total", example=1500.50)


# Schema para crear un registro de Producción
class ProductionCreate(ProductionBase):
    pass


# Schema para devolver un registro de Producción (incluye ID)
class ProductionOut(ProductionBase):
    id: int = Field(..., title="ID del Registro")
    
    class Config:
        from_attributes = True  # Para permitir el uso con modelos SQLAlchemy


# Schema para Clientes (por si lo necesitas en otras operaciones)
class ClienteBase(BaseModel):
    nombre: str = Field(..., max_length=255, title="Nombre del Cliente", example="Juan Pérez")
    cedula_rnc: str = Field(..., max_length=11, title="Cédula o RNC", example="00112345678")
    telefono: str = Field(..., max_length=15, title="Teléfono", example="8095551234")
    direccion: str | None = Field(None, max_length=255, title="Dirección", example="Calle Principal #45")


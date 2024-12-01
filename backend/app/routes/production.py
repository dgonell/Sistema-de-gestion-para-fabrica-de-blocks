from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.production import Production
from app.schemas import ProductionCreate, ProductionOut

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para listar todas las producciones
@router.get("/produccion", response_model=list[ProductionOut])
def list_produccion(db: Session = Depends(get_db)):
    return db.query(Production).all()

# Endpoint para registrar una nueva producción
@router.post("/produccion", response_model=ProductionOut)
def create_produccion(produccion: ProductionCreate, db: Session = Depends(get_db)):
    nueva_produccion = Production(**produccion.dict())
    db.add(nueva_produccion)
    db.commit()
    db.refresh(nueva_produccion)
    return nueva_produccion

# Endpoint para actualizar una producción
@router.put("/produccion/{produccion_id}", response_model=ProductionOut)
def update_produccion(produccion_id: int, produccion: ProductionCreate, db: Session = Depends(get_db)):
    db_produccion = db.query(Production).filter(Production.id == produccion_id).first()
    if not db_produccion:
        raise HTTPException(status_code=404, detail="Producción no encontrada.")
    for key, value in produccion.dict().items():
        setattr(db_produccion, key, value)
    db.commit()
    db.refresh(db_produccion)
    return db_produccion

# Endpoint para eliminar una producción
@router.delete("/produccion/{produccion_id}")
def delete_produccion(produccion_id: int, db: Session = Depends(get_db)):
    db_produccion = db.query(Production).filter(Production.id == produccion_id).first()
    if not db_produccion:
        raise HTTPException(status_code=404, detail="Producción no encontrada.")
    db.delete(db_produccion)
    db.commit()
    return {"message": "Producción eliminada exitosamente."}

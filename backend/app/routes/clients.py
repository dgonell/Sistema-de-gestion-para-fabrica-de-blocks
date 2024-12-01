from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.clients import Cliente
from app.schemas import ClienteCreate, ClienteOut

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para listar todos los clientes
@router.get("/clientes", response_model=list[ClienteOut])
def list_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()

# Endpoint para registrar un cliente
@router.post("/clientes", response_model=ClienteOut)
def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    existing_cliente = db.query(Cliente).filter(Cliente.cedula_rnc == cliente.cedula_rnc).first()
    if existing_cliente:
        raise HTTPException(status_code=400, detail="Cliente con esta cédula/RNC ya existe.")
    new_cliente = Cliente(**cliente.dict())
    db.add(new_cliente)
    db.commit()
    db.refresh(new_cliente)
    return new_cliente

# Endpoint para actualizar un cliente
@router.put("/clientes/{cliente_id}", response_model=ClienteOut)
def update_cliente(cliente_id: int, cliente: ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    for key, value in cliente.dict().items():
        setattr(db_cliente, key, value)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Endpoint para eliminar un cliente
@router.delete("/clientes/{cliente_id}")
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    db.delete(db_cliente)
    db.commit()
    return {"message": "Cliente eliminado exitosamente."}

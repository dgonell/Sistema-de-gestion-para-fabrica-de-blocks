from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.clients import router as clients_router
from app.routes.production import router as production_router
from .database import Base, engine

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI(
    title="Sistema de Blocks",
    description="API para gestionar clientes, producción, almacén y ventas.",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por una lista específica de dominios si quieres restringir el acceso
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Registrar las rutas
app.include_router(clients_router, prefix="/api", tags=["Clientes"])
app.include_router(production_router, prefix="/api", tags=["Producción"])

# Ruta raíz (opcional)
@app.get("/")
def root():
    return {"message": "Bienvenido al API del Sistema de Blocks"}

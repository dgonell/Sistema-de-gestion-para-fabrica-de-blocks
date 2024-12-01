from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuración de la conexión con SQL Server
DATABASE_URL = "mssql+pyodbc://@DESKTOP-9BFQT9D/sistema_blocks?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

# Reemplaza SERVER_NAME con el nombre de tu servidor SQL Server.
# Reemplaza DB_NAME con el nombre de tu base de datos.

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crear una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

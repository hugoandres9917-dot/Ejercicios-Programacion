#database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declarative_base

## conneccion a la base de datos

DATABASE_URL = "sqlite:///lyfter_orm_demo.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def init_db():
    Base.metadata.drop_all(engine) #ELIMINA TODAS LAS TABLAS SI EXISTEN
    Base.metadata.create_all(engine)#VALIDA EXISTANCIA Y CREA SI NO EXISTEN
    print("Base de datos inicializada: tablas varificadas/creadas exitosamente")
    
    
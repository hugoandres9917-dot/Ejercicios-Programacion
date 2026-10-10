#database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declarative_base

DATABASE_URL = "sqlite:///lyfter_orm_demo.db"## conneccion a la base de datos

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def init_db():#mantiene la persitencia de la base de datos, crea las tablas si no existen
    Base.metadata.create_all(engine)#VALIDA EXISTANCIA DE TABLAS, SI NO EXISTEN LAS CREA
    print("Base de datos inicializada: tablas verificadas/creadas exitosamente")
    
    
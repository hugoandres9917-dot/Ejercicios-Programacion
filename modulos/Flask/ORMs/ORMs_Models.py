# Modelos Con SQLAlchemy ORM,
# para crear una base de datos con tablas para usuarios, direcciones y automóviles.

from typing import List, Optional
from sqlalchemy import  ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import DataBase, SessionLocal

# Modelos
class User(DataBase):
    
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    #relaciones ORM
    addresses: Mapped[List["Address"]] = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    vehicles: Mapped[List["Vehicle"]] = relationship("Vehicle", back_populates="user")
    
    def __repr__(self)-> str:
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"


class Address(DataBase):
    
    __tablename__="addresses"
    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(200), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    # FK OBLIGATORIA: las direcciones deben tener un usuario asociado
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="addresses")
    
    def __repr__(self) -> str:
        return f"<Address(id={self.id}, street='{self.street}', city='{self.city}', user_id={self.user_id})>"
    
class Vehicle(DataBase):
    __tablename__= "vehicles"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(50), nullable=False)
    # FK OPCIONAL: los automóviles pueden no tener usuario asociado
    user_id: Mapped[Optional[int]] =mapped_column(ForeignKey("users.id"), nullable=True)
    user: Mapped["User"] = relationship("User", back_populates="vehicles")
    
    def __repr__(self):
        return f"<Vehicle(id={self.id}, brand='{self.brand}', model='{self.model}', user_id={self.user_id})>"
    

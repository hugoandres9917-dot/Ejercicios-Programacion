#user
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[Optional[str]] = mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False) 
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(100), nullable=False, default="user")
    
    invoices: Mapped[List["Invoice"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    contacts: Mapped[List["Contact"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    #Metodo para encriptar y guardar la contraseña
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    #Metodo para verificar si la contraseña coincide al hacer Login
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        }

    def __repr__(self)-> str:
        return f"<User(id={self.id}, username='{self.username}', role='{self.role}')>"
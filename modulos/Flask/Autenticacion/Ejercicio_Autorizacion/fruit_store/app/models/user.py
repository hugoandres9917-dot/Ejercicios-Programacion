#user

#id(entero,primary key)
#username (string, inico obligatorio)
#password_hash (stirng, obligatorio)
#role (string, admin o user por defecto user)

from typing import List, Optional
from sqlalchemy import  ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(DataBase):
    
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255),  nullable=False)
    role: Mapped[str] = mapped_column(String=(100), nullable=False, default="user")
    #relaciones ORM

    def __repr__(self)-> str:
        return f"<User(id={self.id}, username='{self.username}', role='{self.role}')>"

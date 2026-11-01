#contact.py
#Un contacto pertenece a un
# usuario (relación uno a muchos:
# un usuario tiene muchos contactos).
# Necesitamos una llave foránea user_id.

from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app import db

class Contact(db.Model):
    __tablename__ = "contacts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    
    #llave foranea vinculado a users
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    #RELACION INVERSA acceder desde contact
    user: Mapped["User"] = relationship(back_populates="contacts")
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "user_id": self.user_id
        }
        
    def __repr__(self) -> str:
        return  f"<Contact(id={self.id}, name='{self.name}', user_id={self.user_id})>"
#invoice (factura)

from datetime import date
from typing import List, Optional
from sqlalchemy import  ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions.db import db


class Invoice(db.Model):
    
    __tablename__ = "invoices" #minusculas y prural
    
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),  nullable=False)# El user_id es un entero que actua como llave foranea apuntando a la tabla "users"
    user: Mapped["User"] = relationship(back_populates="invoices")# La relacion ORM usa el nombre del modelo entre comillas
    
    # Relacion hacia los detalles de la factura (la tabla intermedia que une factura con productos)
    # invoice_details: Mapped[List["InvoiceDetail"]] = relationship(back_populates="invoice", cascade="all, delete-orphan")
    
    def __repr__(self)-> str:
        return f"<Invoice(id={self.id}, user_id={self.user_id}, date='{self.date}')>"
    

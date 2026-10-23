#Product

# id  (entero, primary key)
#name string obligatorio
#price (float o numeric , obligatorio)
#entry_date (date o datetime, obligario
# stock o queantity (entero, obligatorio)

from datetime import date
from typing import List, Optional
from sqlalchemy import  ForeignKey, String, Float, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions.db import db


class Product(db.Model):
    
    __tablename__ = "products" #minusculas y prural
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float,  nullable=False)
    entry_date: Mapped[date] = mapped_column(Date, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    # Relación ORM (más adelante la conectaremos con los detalles de la factura)
    # invoice_details: Mapped[List["InvoiceDetail"]] = relationship(back_populates="product")
    
    
    def __repr__(self)-> str:
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, stock='{self.stock}')>"

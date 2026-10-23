#Invoice_Detail (tabla intermedia)


from datetime import date
from typing import List, Optional
from sqlalchemy import  ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions.db import db


class InvoiceDetail(db.Model):
    
    __tablename__ = "invoices_details" #minusculas y prural
    
    id: Mapped[int] = mapped_column(primary_key=True)
    #LLAVES FOREANEAS
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"),  nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"),  nullable=False)
    #DATOS DE LINEA DE VENTA
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Relaciones ORM OPCIONALES RECOMENDADAS
    invoice: Mapped['Invoice'] = relationship(back_populates="invoice_details")
    product: Mapped["Product"] = relationship(back_populates="invoice_details")
    
    def __repr__(self)-> str:
        return f"<InvoiceDetail(id={self.id}, invoice_id={self.invoice_id}, product_id={self.product_id}, quantity={self.quantity})>"
    

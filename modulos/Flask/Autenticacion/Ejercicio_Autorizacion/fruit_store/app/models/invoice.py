#invoice (factura)

from datetime import date
from typing import List
from sqlalchemy import ForeignKey, Date, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db

class Invoice(db.Model):
    __tablename__ = "invoices"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    
    # Relación con el usuario
    user: Mapped["User"] = relationship(back_populates="invoices")
    invoice_details: Mapped[List["InvoiceDetail"]] = relationship(back_populates="invoice", cascade="all, delete-orphan")
    
    def serialize(self):
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "user_id": self.user_id,
            "total_amount": self.total_amount,
            "invoice_details": [detail.serialize() for detail in self.invoice_details]
        }
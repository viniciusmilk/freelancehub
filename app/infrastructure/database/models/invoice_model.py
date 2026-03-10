from sqlalchemy import String, Float, Enum, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.infrastructure.database.base_model import BaseModel
from app.domain.enums import InvoiceStatus

class InvoiceModel(BaseModel):
    __tablename__ = 'invoices'
    
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[InvoiceStatus] = mapped_column(
        Enum(InvoiceStatus, name='invoice_status'), nullable=False,
    )
    due_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    issued_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    paid_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    contract_id: Mapped[str] = mapped_column(
        ForeignKey("contracts.id"),
        nullable=False,
        index=True,
    )
    
    contract = relationship("ContractModel", back_populates="invoices")
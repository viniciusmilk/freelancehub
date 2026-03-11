#Invoice Model
from datetime import datetime

from sqlalchemy import (
    DateTime,
    Enum,
    Float,
    ForeignKey,
    CheckConstraint,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.domain.enums import InvoiceStatus
from app.infrastructure.database.base_model import BaseModel


class InvoiceModel(BaseModel):
    __tablename__ = 'invoices'
    __table_args__ = (
        CheckConstraint('amount >= 0', name='check_amount_non_negative'),
    )

    amount: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[InvoiceStatus] = mapped_column(
        Enum(InvoiceStatus, name='invoice_status'), nullable=False,
    )
    due_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    issued_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    paid_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    contract_id: Mapped[str] = mapped_column(
        ForeignKey("contracts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    contract = relationship("ContractModel", back_populates="invoices")

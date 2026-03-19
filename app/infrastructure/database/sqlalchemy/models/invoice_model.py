# Invoice Model
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    ForeignKey,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.domain.enums import InvoiceStatus

from ..base_model import BaseModel


class InvoiceModel(BaseModel):
    __tablename__ = 'invoices'
    __table_args__ = (
        CheckConstraint('amount >= 0', name='check_amount_non_negative'),
    )

    invoice_number: Mapped[str] = mapped_column(
        String(50), nullable=False, unique=True
    )
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    tax_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2), nullable=False, default=0
    )
    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2), nullable=False
    )
    status: Mapped[InvoiceStatus] = mapped_column(
        Enum(InvoiceStatus, name='invoice_status'),
        nullable=False,
        default=InvoiceStatus.draft,
    )
    due_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    issued_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    paid_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    payment_method: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )
    payment_reference: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    contract_id: Mapped[str] = mapped_column(
        ForeignKey('contracts.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    milestone_id: Mapped[str | None] = mapped_column(
        ForeignKey('milestones.id', ondelete='SET NULL'),
        nullable=True,
        index=True,
    )

    # Relationships
    contract = relationship('ContractModel', back_populates='invoices')
    milestone = relationship('MilestoneModel', back_populates='invoices')

    notifications = relationship(
        'NotificationModel',
        back_populates='invoice',
        cascade='all, delete-orphan',
    )

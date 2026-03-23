# Contract Model
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    Enum,
    ForeignKey,
    Numeric,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.domain.enums import ContractStatus

from ..base_model import BaseModel


class ContractModel(BaseModel):
    __tablename__ = 'contracts'
    __table_args__ = (
        CheckConstraint('value >= 0', name='check_value_non_negative'),
    )

    terms: Mapped[str] = mapped_column(Text, nullable=False)
    value: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    status: Mapped[ContractStatus] = mapped_column(
        Enum(ContractStatus, name='contract_status'),
        nullable=False,
        default=ContractStatus.draft,
    )
    signed: Mapped[bool] = mapped_column(Boolean, default=False)
    signed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    started_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    termination_reason: Mapped[str | None] = mapped_column(Text, nullable=True)

    project_id: Mapped[str] = mapped_column(
        ForeignKey('projects.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    freelancer_id: Mapped[str] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    proposal_id: Mapped[str | None] = mapped_column(
        ForeignKey('proposals.id', ondelete='SET NULL'),
        nullable=True,
        index=True,
    )

    # Relationships
    project = relationship('ProjectModel', back_populates='contracts')
    freelancer = relationship('UserModel', back_populates='contracts')
    proposal = relationship('ProposalModel', back_populates='contract')

    invoices = relationship(
        'InvoiceModel',
        back_populates='contract',
        cascade='all, delete-orphan',
    )

    reviews = relationship(
        'ReviewModel',
        back_populates='contract',
        cascade='all, delete-orphan',
    )

    notifications = relationship(
        'NotificationModel',
        back_populates='contract',
        cascade='all, delete-orphan',
    )

    milestones = relationship(
        'MilestoneModel',
        back_populates='contract',
        cascade='all, delete-orphan',
    )

    time_entries = relationship(
        'TimeEntryModel',
        back_populates='contract',
        cascade='all, delete-orphan',
    )

    messages = relationship(
        'MessageModel',
        back_populates='contract',
        cascade='all, delete-orphan',
    )

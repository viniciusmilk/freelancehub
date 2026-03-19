# Milestone Model
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

from app.domain.enums import MilestoneStatus

from ..base_model import BaseModel


class MilestoneModel(BaseModel):
    __tablename__ = 'milestones'
    __table_args__ = (
        CheckConstraint('amount >= 0', name='check_amount_non_negative'),
        CheckConstraint(
            'progress_percentage >= 0 AND progress_percentage <= 100',
            name='check_progress_percentage_range',
        ),
    )

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    due_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[MilestoneStatus] = mapped_column(
        Enum(MilestoneStatus, name='milestone_status'),
        nullable=False,
        default=MilestoneStatus.pending,
    )
    progress_percentage: Mapped[float] = mapped_column(
        nullable=False, default=0.0
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    approved_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    project_id: Mapped[str] = mapped_column(
        ForeignKey('projects.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )

    # Relationships
    project = relationship('ProjectModel', back_populates='milestones')

    time_entries = relationship(
        'TimeEntryModel',
        back_populates='milestone',
        cascade='all, delete-orphan',
    )

    invoices = relationship(
        'InvoiceModel',
        back_populates='milestone',
        cascade='all, delete-orphan',
    )

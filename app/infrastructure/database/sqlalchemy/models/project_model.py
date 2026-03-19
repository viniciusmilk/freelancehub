# Project Model
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    ForeignKey,
    Numeric,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.domain.enums import ProjectStatus

from ..base_model import BaseModel


class ProjectModel(BaseModel):
    __tablename__ = 'projects'
    __table_args__ = (
        CheckConstraint(
            'budget >= 0',
            name='check_budget_non_negative',
        ),
        UniqueConstraint('title', name='uq_title'),
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    status: Mapped[ProjectStatus] = mapped_column(
        Enum(ProjectStatus, name='project_status'),
        nullable=False,
        default=ProjectStatus.draft,
    )
    budget: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    start_date: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    end_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    skills_required: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_remote: Mapped[bool] = mapped_column(nullable=False, default=True)
    client_id: Mapped[str] = mapped_column(
        ForeignKey('clients.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )

    # Relationships
    client = relationship('ClientModel', back_populates='projects')

    proposals = relationship(
        'ProposalModel', back_populates='project', cascade='all, delete-orphan'
    )

    contracts = relationship(
        'ContractModel', back_populates='project', cascade='all, delete-orphan'
    )

    milestones = relationship(
        'MilestoneModel',
        back_populates='project',
        cascade='all, delete-orphan',
    )

    time_entries = relationship(
        'TimeEntryModel',
        back_populates='project',
        cascade='all, delete-orphan',
    )

    reviews = relationship(
        'ReviewModel', back_populates='project', cascade='all, delete-orphan'
    )

    notifications = relationship(
        'NotificationModel',
        back_populates='project',
        cascade='all, delete-orphan',
    )

# Proposal Model
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
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

from app.domain.enums import ProposalStatus

from ..base_model import BaseModel


class ProposalModel(BaseModel):
    __tablename__ = 'proposals'
    __table_args__ = (
        CheckConstraint(
            'estimated_budget >= 0', name='check_estimated_budget_non_negative'
        ),
        CheckConstraint(
            'estimated_hours >= 0', name='check_estimated_hours_non_negative'
        ),
    )

    cover_letter: Mapped[str] = mapped_column(Text, nullable=False)
    estimated_budget: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False
    )
    estimated_hours: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[ProposalStatus] = mapped_column(
        Enum(ProposalStatus, name='proposal_status'),
        nullable=False,
        default=ProposalStatus.draft,
    )
    submitted_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    reviewed_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

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

    # Relationships
    project = relationship('ProjectModel', back_populates='proposals')
    freelancer = relationship('UserModel', back_populates='proposals')

    contract = relationship(
        'ContractModel',
        back_populates='proposal',
        uselist=False,
        cascade='all, delete-orphan',
    )

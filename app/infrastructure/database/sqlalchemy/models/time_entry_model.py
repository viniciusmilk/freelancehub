# Time Entry Model
from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.domain.enums import TimeEntryStatus

from ..base_model import BaseModel


class TimeEntryModel(BaseModel):
    __tablename__ = 'time_entries'
    __table_args__ = (
        CheckConstraint('hours >= 0', name='check_hours_non_negative'),
        CheckConstraint('hours <= 24', name='check_hours_daily_limit'),
    )

    description: Mapped[str] = mapped_column(Text, nullable=False)
    hours: Mapped[float] = mapped_column(nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[TimeEntryStatus] = mapped_column(
        Enum(TimeEntryStatus, name='time_entry_status'),
        nullable=False,
        default=TimeEntryStatus.draft,
    )
    submitted_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    approved_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    freelancer_id: Mapped[str] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    project_id: Mapped[str] = mapped_column(
        ForeignKey('projects.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    milestone_id: Mapped[str | None] = mapped_column(
        ForeignKey('milestones.id', ondelete='SET NULL'),
        nullable=True,
        index=True,
    )

    # Relationships
    freelancer = relationship('UserModel', back_populates='time_entries')
    project = relationship('ProjectModel', back_populates='time_entries')
    milestone = relationship('MilestoneModel', back_populates='time_entries')

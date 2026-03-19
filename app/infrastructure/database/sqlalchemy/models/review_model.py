# Review Model
from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from ..base_model import BaseModel


class ReviewModel(BaseModel):
    __tablename__ = 'reviews'
    __table_args__ = (
        CheckConstraint(
            'rating >= 1 AND rating <= 5', name='check_rating_range'
        ),
        CheckConstraint(
            'communication_rating >= 1 AND communication_rating <= 5',
            name='check_communication_rating_range',
        ),
        CheckConstraint(
            'quality_rating >= 1 AND quality_rating <= 5',
            name='check_quality_rating_range',
        ),
        CheckConstraint(
            'deadline_rating >= 1 AND deadline_rating <= 5',
            name='check_deadline_rating_range',
        ),
    )

    rating: Mapped[float] = mapped_column(nullable=False)
    communication_rating: Mapped[float] = mapped_column(nullable=False)
    quality_rating: Mapped[float] = mapped_column(nullable=False)
    deadline_rating: Mapped[float] = mapped_column(nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    is_public: Mapped[bool] = mapped_column(nullable=False, default=True)
    responded_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    response: Mapped[str | None] = mapped_column(Text, nullable=True)

    project_id: Mapped[str] = mapped_column(
        ForeignKey('projects.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    reviewer_id: Mapped[str] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    reviewee_id: Mapped[str] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    contract_id: Mapped[str] = mapped_column(
        ForeignKey('contracts.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )

    # Relationships
    project = relationship('ProjectModel', back_populates='reviews')
    reviewer = relationship(
        'UserModel', foreign_keys=[reviewer_id], back_populates='reviews_given'
    )
    reviewee = relationship(
        'UserModel',
        foreign_keys=[reviewee_id],
        back_populates='reviews_received',
    )
    contract = relationship('ContractModel', back_populates='reviews')

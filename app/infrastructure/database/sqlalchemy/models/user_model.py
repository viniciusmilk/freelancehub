# User Model
from typing import Optional

from sqlalchemy import (
    Enum,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.domain.enums import UserRole

from ..base_model import BaseModel
from .client_model import ClientModel


class UserModel(BaseModel):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint('email', name='uq_email'),
        UniqueConstraint('username', name='uq_username'),
    )
    username: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )
    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    password_hash: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name='user_role'),
        nullable=False,
    )
    oauth_provider: Mapped[Optional[str]] = mapped_column(
        String,
        nullable=True,
    )
    phone: Mapped[Optional[str]] = mapped_column(
        String(20),
        nullable=True,
    )
    bio: Mapped[Optional[str]] = mapped_column(
        String(1000),
        nullable=True,
    )
    skills: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
    )
    hourly_rate: Mapped[Optional[float]] = mapped_column(
        nullable=True,
    )
    is_available: Mapped[bool] = mapped_column(
        nullable=False,
        default=True,
    )
    profile_image_url: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
    )

    # Relationships
    clients: Mapped[list['ClientModel']] = relationship(
        'ClientModel',
        back_populates='owner',
        cascade='all, delete-orphan',
    )

    proposals = relationship(
        'ProposalModel',
        back_populates='freelancer',
        cascade='all, delete-orphan',
    )

    contracts = relationship(
        'ContractModel',
        back_populates='freelancer',
        cascade='all, delete-orphan',
    )

    time_entries = relationship(
        'TimeEntryModel',
        back_populates='freelancer',
        cascade='all, delete-orphan',
    )

    reviews_given = relationship(
        'ReviewModel',
        foreign_keys='ReviewModel.reviewer_id',
        back_populates='reviewer',
        cascade='all, delete-orphan',
    )

    reviews_received = relationship(
        'ReviewModel',
        foreign_keys='ReviewModel.reviewee_id',
        back_populates='reviewee',
        cascade='all, delete-orphan',
    )

    notifications = relationship(
        'NotificationModel',
        back_populates='user',
        cascade='all, delete-orphan',
    )

    sent_messages = relationship(
        'MessageModel',
        foreign_keys='MessageModel.sender_id',
        back_populates='sender',
        cascade='all, delete-orphan',
    )

    received_messages = relationship(
        'MessageModel',
        foreign_keys='MessageModel.receiver_id',
        back_populates='receiver',
        cascade='all, delete-orphan',
    )

# Message Model
from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from ..base_model import BaseModel


class MessageModel(BaseModel):
    __tablename__ = 'messages'

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )
    content: Mapped[str] = mapped_column(String(1000), nullable=False)
    sender_id: Mapped[str] = mapped_column(
        ForeignKey('users.id'), ondelete='CASCADE', nullable=False, index=True
    )
    receiver_id: Mapped[str] = mapped_column(
        ForeignKey('users.id'), ondelete='CASCADE', nullable=False, index=True
    )
    contract_id: Mapped[str] = mapped_column(
        ForeignKey('contracts.id'),
        ondelete='CASCADE',
        nullable=True,
        index=True,
    )
    project_id: Mapped[str] = mapped_column(
        ForeignKey('projects.id'),
        ondelete='CASCADE',
        nullable=True,
        index=True,
    )
    read: Mapped[bool] = mapped_column(Boolean, default=False)
    read_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    # relationships
    contract = relationship('ContractModel', back_populates='messages')
    project = relationship('ProjectModel', back_populates='messages')
    sender = relationship(
        'UserModel', foreign_keys=[sender_id], back_populates='sent_messages'
    )
    receiver = relationship(
        'UserModel',
        foreign_keys=[receiver_id],
        back_populates='received_messages',
    )

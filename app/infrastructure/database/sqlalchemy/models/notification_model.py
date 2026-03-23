# Notification Model
from datetime import datetime

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.domain.enums import NotificationType

from ..base_model import BaseModel


class NotificationModel(BaseModel):
    __tablename__ = 'notifications'

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    type: Mapped[NotificationType] = mapped_column(
        Enum(NotificationType, name='notification_type'),
        nullable=False,
    )
    is_read: Mapped[bool] = mapped_column(nullable=False, default=False)
    read_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    scheduled_for: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    notification_metadata: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )

    project_id: Mapped[str | None] = mapped_column(
        ForeignKey('projects.id', ondelete='SET NULL'),
        nullable=True,
        index=True,
    )
    contract_id: Mapped[str | None] = mapped_column(
        ForeignKey('contracts.id', ondelete='SET NULL'),
        nullable=True,
        index=True,
    )
    invoice_id: Mapped[str | None] = mapped_column(
        ForeignKey('invoices.id', ondelete='SET NULL'),
        nullable=True,
        index=True,
    )

    # Relationships
    user = relationship('UserModel', back_populates='notifications')
    project = relationship('ProjectModel', back_populates='notifications')
    contract = relationship('ContractModel', back_populates='notifications')
    invoice = relationship('InvoiceModel', back_populates='notifications')

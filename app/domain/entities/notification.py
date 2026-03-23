from datetime import datetime
from typing import Optional
from uuid import UUID

from ..enums import NotificationType
from .base_entity import BaseEntity


class Notification(BaseEntity):
    def __init__(
        self,
        id: UUID,
        title: str,
        message: str,
        type: NotificationType,
        user_id: UUID,
        created_at: datetime,
        is_read: bool = False,
        read_at: Optional[datetime] = None,
        scheduled_for: Optional[datetime] = None,
        metadata: Optional[str] = None,
        project_id: Optional[UUID] = None,
        contract_id: Optional[UUID] = None,
        invoice_id: Optional[UUID] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.user_id = user_id
        self.project_id = project_id
        self.contract_id = contract_id
        self.invoice_id = invoice_id
        self.type = type
        self.title = title
        self.message = message
        self.is_read = is_read
        self.read_at = read_at
        self.scheduled_for = scheduled_for
        self.notification_metadata = metadata

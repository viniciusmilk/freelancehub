from datetime import datetime
from typing import Optional
from uuid import UUID

from .base_entity import BaseEntity


class Message(BaseEntity):
    def __init__(
        self,
        id: UUID,
        sender_id: UUID,
        receiver_id: UUID,
        content: str,
        created_at: datetime,
        contract_id: Optional[UUID] = None,
        project_id: Optional[UUID] = None,
        read: bool = False,
        read_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.project_id = project_id
        self.contract_id = contract_id
        self.content = content
        self.read = read
        self.read_at = read_at

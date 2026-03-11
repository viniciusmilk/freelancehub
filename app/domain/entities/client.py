from datetime import datetime
from typing import Optional
from uuid import UUID

from .base_entity import BaseEntity


class Client(BaseEntity):
    def __init__(
        self,
        id: UUID,
        name: str,
        description: str,
        owner_id: UUID,
        created_at: datetime,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.name = name
        self.description = description
        self.owner_id = owner_id

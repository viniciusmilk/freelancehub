#base   
from datetime import datetime
from typing import Optional
from uuid import UUID


class BaseEntity:
    def __init__(
        self,
        id: UUID,
        created_at: datetime,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

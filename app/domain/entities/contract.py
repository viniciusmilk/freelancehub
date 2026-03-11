from datetime import datetime
from typing import Optional
from uuid import UUID

from .base_entity import BaseEntity


class Contract(BaseEntity):
    def __init__(
        self,
        id: UUID,
        project_id: UUID,
        terms: str,
        value: float,
        signed: bool,
        created_at: datetime,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.project_id = project_id
        self.terms = terms
        self.value = value
        self.signed = signed

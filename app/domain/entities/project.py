from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from ..enums import ProjectStatus
from .base_entity import BaseEntity


class Project(BaseEntity):
    def __init__(
        self,
        id: UUID,
        title: str,
        description: str,
        status: ProjectStatus,
        budget: Decimal,
        client_id: UUID,
        skills_required: Optional[str],
        is_remote: bool,
        start_date: Optional[datetime],
        end_date: Optional[datetime],
        location: Optional[str],
        created_at: datetime,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.title = title
        self.description = description
        self.status = status
        self.budget = budget
        self.client_id = client_id
        self.skills_required = skills_required
        self.is_remote = is_remote
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

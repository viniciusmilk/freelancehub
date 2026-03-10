# project
from datetime import datetime
from typing import Optional
from uuid import UUID

from app.domain.enums import ProjectStatus

from .base_entity import BaseEntity


class Project(BaseEntity):
    def __init__(
        self,
        id: UUID,
        title: str,
        description: str,
        status: ProjectStatus,
        budget: float,
        client_id: UUID,
        freelancer_id: UUID,
        created_at: datetime,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.title = title
        self.description = description
        self.status = status
        self.budget = budget
        self.client_id = client_id
        self.freelancer_id = freelancer_id

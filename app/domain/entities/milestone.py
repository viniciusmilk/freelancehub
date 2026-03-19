from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from ..enums import MilestoneStatus
from .base_entity import BaseEntity


class Milestone(BaseEntity):
    def __init__(
        self,
        id: UUID,
        title: str,
        description: str,
        amount: Decimal,
        status: MilestoneStatus,
        due_date: datetime,
        project_id: UUID,
        created_at: datetime,
        progress_percentage: float = 0.0,
        completed_at: Optional[datetime] = None,
        approved_at: Optional[datetime] = None,
        notes: Optional[str] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.project_id = project_id
        self.title = title
        self.description = description
        self.amount = amount
        self.status = status
        self.due_date = due_date
        self.progress_percentage = progress_percentage
        self.completed_at = completed_at
        self.approved_at = approved_at
        self.notes = notes

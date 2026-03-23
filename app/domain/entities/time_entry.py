from datetime import datetime
from typing import Optional
from uuid import UUID

from ..enums import TimeEntryStatus
from .base_entity import BaseEntity


class TimeEntry(BaseEntity):
    def __init__(
        self,
        id: UUID,
        description: str,
        hours: float,
        date: datetime,
        status: TimeEntryStatus,
        freelancer_id: UUID,
        contract_id: UUID,
        created_at: datetime,
        milestone_id: Optional[UUID] = None,
        submitted_at: Optional[datetime] = None,
        approved_at: Optional[datetime] = None,
        notes: Optional[str] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.freelancer_id = freelancer_id
        self.contract_id = contract_id
        self.milestone_id = milestone_id
        self.hours = hours
        self.description = description
        self.date = date
        self.status = status
        self.submitted_at = submitted_at
        self.approved_at = approved_at
        self.notes = notes

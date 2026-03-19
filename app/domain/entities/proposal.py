from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from ..enums import ProposalStatus
from .base_entity import BaseEntity


class Proposal(BaseEntity):
    def __init__(
        self,
        id: UUID,
        cover_letter: str,
        estimated_budget: Decimal,
        estimated_hours: float,
        status: ProposalStatus,
        project_id: UUID,
        freelancer_id: UUID,
        created_at: datetime,
        submitted_at: Optional[datetime] = None,
        reviewed_at: Optional[datetime] = None,
        notes: Optional[str] = None,
        contract_id: Optional[UUID] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.cover_letter = cover_letter
        self.estimated_budget = estimated_budget
        self.estimated_hours = estimated_hours
        self.status = status
        self.project_id = project_id
        self.freelancer_id = freelancer_id
        self.submitted_at = submitted_at
        self.reviewed_at = reviewed_at
        self.notes = notes
        self.contract_id = contract_id

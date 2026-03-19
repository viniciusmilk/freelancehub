from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from ..enums import ContractStatus
from .base_entity import BaseEntity


class Contract(BaseEntity):
    def __init__(
        self,
        id: UUID,
        terms: str,
        value: Decimal,
        status: ContractStatus,
        project_id: UUID,
        freelancer_id: UUID,
        created_at: datetime,
        signed: bool = False,
        signed_at: Optional[datetime] = None,
        started_at: Optional[datetime] = None,
        completed_at: Optional[datetime] = None,
        termination_reason: Optional[str] = None,
        proposal_id: Optional[UUID] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.project_id = project_id
        self.freelancer_id = freelancer_id
        self.proposal_id = proposal_id
        self.terms = terms
        self.value = value
        self.signed = signed
        self.status = status
        self.signed_at = signed_at
        self.started_at = started_at
        self.completed_at = completed_at
        self.termination_reason = termination_reason

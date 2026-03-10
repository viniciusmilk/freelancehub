#invoice
from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from app.domain.enums import InvoiceStatus

from .base_entity import BaseEntity


class Invoice(BaseEntity):
    def __init__(
        self,
        id: UUID,
        contract_id: UUID,
        amount: Decimal,
        status: InvoiceStatus,
        due_date: datetime,
        created_at: datetime,
        issued_at: Optional[datetime] = None,
        paid_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.contract_id = contract_id
        self.amount = amount
        self.status = status
        self.due_date = due_date
        self.issued_at = issued_at
        self.paid_at = paid_at

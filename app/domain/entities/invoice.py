from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from ..enums import InvoiceStatus
from .base_entity import BaseEntity


class Invoice(BaseEntity):
    def __init__(
        self,
        id: UUID,
        invoice_number: str,
        amount: Decimal,
        tax_amount: Decimal,
        total_amount: Decimal,
        status: InvoiceStatus,
        due_date: datetime,
        contract_id: UUID,
        created_at: datetime,
        issued_at: Optional[datetime] = None,
        paid_at: Optional[datetime] = None,
        notes: Optional[str] = None,
        payment_method: Optional[str] = None,
        payment_reference: Optional[str] = None,
        milestone_id: Optional[UUID] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(id, created_at, updated_at)
        self.invoice_number = invoice_number
        self.amount = amount
        self.tax_amount = tax_amount
        self.total_amount = total_amount
        self.status = status
        self.due_date = due_date
        self.contract_id = contract_id
        self.milestone_id = milestone_id
        self.issued_at = issued_at
        self.paid_at = paid_at
        self.notes = notes
        self.payment_method = payment_method
        self.payment_reference = payment_reference

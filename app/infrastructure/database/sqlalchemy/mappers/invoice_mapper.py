from uuid import UUID

from .....domain.entities import Invoice
from ..models.invoice_model import InvoiceModel
from .base_mapper import BaseMapper


class InvoiceMapper(BaseMapper[Invoice, InvoiceModel]):
    @staticmethod
    def to_entity(model: InvoiceModel) -> Invoice:
        return Invoice(
            id=UUID(model.id),
            project_id=UUID(model.project_id),
            amount=model.amount,
            status=model.status,
            due_date=model.due_date,
            issued_at=model.issued_at,
            paid_at=model.paid_at,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def to_model(entity: Invoice) -> InvoiceModel:
        return InvoiceModel(
            id=str(entity.id),
            project_id=str(entity.project_id),
            amount=entity.amount,
            status=entity.status,
            due_date=entity.due_date,
            issued_at=entity.issued_at,
            paid_at=entity.paid_at,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

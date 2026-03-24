from decimal import Decimal
from typing import List, Optional

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .....domain.entities import Invoice
from .....domain.enums import InvoiceStatus
from ..mappers import InvoiceMapper
from ..models import ContractModel, InvoiceModel, ProjectModel
from .base_repository import BaseRepository


class InvoiceRepository(BaseRepository[Invoice, InvoiceModel]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model_class=InvoiceModel,
            mapper=InvoiceMapper,
        )

    def get_by_contract(self, contract_id: str) -> Optional[List[Invoice]]:
        stmt = select(self.model_class).where(
            self.model_class.contract_id == contract_id
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_by_freelancer(self, freelancer_id: str) -> Optional[List[Invoice]]:
        stmt = (
            select(self.model_class)
            .join(self.model_class.contract)
            .where(ContractModel.freelancer_id == freelancer_id)
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_by_client(self, client_id: str) -> Optional[List[Invoice]]:
        stmt = (
            select(self.model_class)
            .join(self.model_class.contract)
            .join(self.model_class.contract.project)
            .where(ProjectModel.client_id == client_id)
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_by_milestone(self, milestone_id: str) -> Optional[List[Invoice]]:
        stmt = select(self.model_class).where(
            self.model_class.milestone_id == milestone_id
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_by_status(self, status: InvoiceStatus) -> Optional[List[Invoice]]:
        stmt = select(self.model_class).where(
            self.model_class.status == status
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_pending(self) -> Optional[List[Invoice]]:
        stmt = select(self.model_class).where(
            self.model_class.status == InvoiceStatus.pending
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_overdue(self) -> Optional[List[Invoice]]:
        stmt = select(self.model_class).where(
            self.model_class.status == InvoiceStatus.overdue
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_paid(self) -> Optional[List[Invoice]]:
        stmt = select(self.model_class).where(
            self.model_class.status == InvoiceStatus.paid
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_cancelled(self) -> Optional[List[Invoice]]:
        stmt = select(self.model_class).where(
            self.model_class.status == InvoiceStatus.cancelled
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_total_pending_amount(self) -> Decimal:
        stmt = select(func.sum(self.model_class.amount)).where(
            self.model_class.status == InvoiceStatus.pending
        )
        result = self.session.execute(stmt)
        return result.scalar() or Decimal('0')

    def get_total_overdue_amount(self) -> Decimal:
        stmt = select(func.sum(self.model_class.amount)).where(
            self.model_class.status == InvoiceStatus.overdue
        )
        result = self.session.execute(stmt)
        return result.scalar() or Decimal('0')

    def get_total_paid_amount(self) -> Decimal:
        stmt = select(func.sum(self.model_class.amount)).where(
            self.model_class.status == InvoiceStatus.paid
        )
        result = self.session.execute(stmt)
        return result.scalar() or Decimal('0')

    def get_total_cancelled_amount(self) -> Decimal:
        stmt = select(func.sum(self.model_class.amount)).where(
            self.model_class.status == InvoiceStatus.cancelled
        )
        result = self.session.execute(stmt)
        return result.scalar() or Decimal('0')

    def get_total_earned_by_freelancer(self, freelancer_id: str) -> Decimal:
        stmt = (
            select(func.sum(self.model_class.amount))
            .join(self.model_class.contract)
            .join(ContractModel.project)
            .where(
                ProjectModel.freelancer_id == freelancer_id,
                self.model_class.status == InvoiceStatus.paid,
            )
        )
        result = self.session.execute(stmt)
        return result.scalar() or Decimal('0')

    def get_monthly_revenue(self, freelancer_id: str) -> List:
        stmt = (
            select(
                func.extract('year', self.model_class.created_at).label(
                    'year'
                ),
                func.extract('month', self.model_class.created_at).label(
                    'month'
                ),
                func.sum(self.model_class.amount).label('total_revenue'),
            )
            .join(self.model_class.contract)
            .where(
                ContractModel.freelancer_id == freelancer_id,
                self.model_class.status == InvoiceStatus.paid,
            )
            .group_by(
                func.extract('year', self.model_class.created_at),
                func.extract('month', self.model_class.created_at),
            )
            .order_by(
                func.extract('year', self.model_class.created_at),
                func.extract('month', self.model_class.created_at),
            )
        )

        result = self.session.execute(stmt)
        return result.all()

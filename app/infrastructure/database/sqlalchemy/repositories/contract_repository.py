from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from .....domain.entities import Contract
from ..mappers import ContractMapper
from ..models import ContractModel, ProjectModel
from .base_repository import BaseRepository


class ContractRepository(BaseRepository[Contract, ContractModel]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model_class=ContractModel,
            mapper=ContractMapper,
        )

    def get_by_project(self, project_id: str) -> List[Contract]:
        stmt = select(self.model_class).where(
            self.model_class.project_id == project_id
        )
        result = self.session.execute(stmt)

        models = result.scalars().all()

        if not models:
            return []

        return [self.mapper.to_entity(model) for model in models]

    def get_signed_by_project(
        self, project_id: str
    ) -> Optional[List[Contract]]:
        stmt = select(self.model_class).where(
            self.model_class.project_id == project_id,
            self.model_class.signed.is_(True),
        )
        result = self.session.execute(stmt)

        models = result.scalars().all()

        if not models:
            return []

        return [self.mapper.to_entity(model) for model in models]

    def get_by_freelancer(self, freelancer_id: str) -> List[Contract]:
        stmt = select(self.model_class).where(
            self.model_class.freelancer_id == freelancer_id
        )
        result = self.session.execute(stmt)

        models = result.scalars().all()

        if not models:
            return []

        return [self.mapper.to_entity(model) for model in models]

    def get_by_client(self, client_id: str) -> List[Contract]:
        stmt = select(self.model_class).join(
            ProjectModel
        ).where(
            ProjectModel.client_id == client_id
        )
        result = self.session.execute(stmt)

        models = result.scalars().all()

        if not models:
            return []

        return [self.mapper.to_entity(model) for model in models]

    def get_by_project_and_id(
        self, project_id: str, id: str
    ) -> Optional[Contract]:
        stmt = select(self.model_class).where(
            self.model_class.project_id == project_id,
            self.model_class.id == id,
        )
        result = self.session.execute(stmt)

        model = result.scalars().first()

        if not model:
            return None

        return self.mapper.to_entity(model)

    def get_with_invoices(self, id: str) -> Optional[List[Contract]]:
        pass

from typing import List, Optional

from sqlalchemy import select

from .....domain.entities import Client
from ..mappers import ClientMapper
from ..models import ClientModel
from .base_repository import BaseRepository


class ClientRepository(BaseRepository[Client, ClientModel]):
    def __init__(self, session):
        super().__init__(
            session=session,
            model_class=ClientModel,
            mapper=ClientMapper,
        )

    def get_by_owner(self, owner_id: str) -> Optional[List[Client]]:
        stmt = select(self.model_class).where(
            self.model_class.owner_id == owner_id
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_by_name(self, name: str):
        stmt = select(self.model_class).where(self.model_class.name == name)
        result = self.session.execute(stmt)
        model = result.scalars().one_or_none()

        if not model:
            return None

        return self.mapper.to_entity(model)

    def get_by_owner_and_id(self, owner_id: str, client_id: str):
        stmt = select(self.model_class).where(
            self.model_class.owner_id == owner_id,
            self.model_class.id == client_id,
        )
        result = self.session.execute(stmt)
        model = result.scalars().one_or_none()

        if not model:
            return None

        return self.mapper.to_entity(model)

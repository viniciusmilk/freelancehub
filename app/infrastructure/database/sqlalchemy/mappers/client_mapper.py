from uuid import UUID

from .....domain.entities import Client
from ..models import ClientModel
from .base_mapper import BaseMapper


class ClientMapper(BaseMapper[Client, ClientModel]):
    @staticmethod
    def to_entity(model: ClientModel) -> Client:
        return Client(
            id=UUID(model.id),
            name=model.name,
            description=model.description,
            owner_id=UUID(model.owner_id),
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def to_model(entity: Client) -> ClientModel:
        return ClientModel(
            id=str(entity.id),
            name=entity.name,
            description=entity.description,
            owner_id=str(entity.owner_id),
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

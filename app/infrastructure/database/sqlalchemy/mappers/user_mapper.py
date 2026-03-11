from uuid import UUID

from .....domain.entities import User
from ..models.user_model import UserModel

from .base_mapper import BaseMapper


class UserMapper(BaseMapper[User, UserModel]):
    @staticmethod
    def to_entity(model: UserModel) -> User:
        return User(
            id=UUID(model.id),
            username=model.username,
            email=model.email,
            first_name=model.first_name,
            last_name=model.last_name,
            password_hash=model.password_hash,
            role=model.role,
            oauth_provider=model.oauth_provider,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def to_model(entity: User) -> UserModel:
        return UserModel(
            id=str(entity.id),
            username=entity.username,
            email=entity.email,
            first_name=entity.first_name,
            last_name=entity.last_name,
            password_hash=entity.password_hash,
            role=entity.role,
            oauth_provider=entity.oauth_provider,
        )

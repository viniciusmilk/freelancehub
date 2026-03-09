from uuid import UUID

from app.domain.entities.users import User
from app.infrastructure.database.models.user_model import UserModel

from .base_mapper import BaseMapper


class UserMapper(BaseMapper[User, UserModel]):
    @staticmethod
    def to_entity(model: UserModel) -> User:
        return User(
            id=UUID(model.id),
            username=model.username,
            email=model.email,
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
            password_hash=entity.password_hash,
            role=entity.role,
            oauth_provider=entity.oauth_provider,
        )

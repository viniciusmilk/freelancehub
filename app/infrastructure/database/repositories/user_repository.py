from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.entities.users import User
from app.infrastructure.database.mappers.user_mapper import UserMapper
from app.infrastructure.database.models import UserModel
from app.infrastructure.database.repositories.base_repository import (
    BaseRepository,
)


class UserRepository(BaseRepository[User, UserModel]):
    def __init__(self, session: Session):
        super().__init__(
            session=session, model_class=UserModel, mapper=UserMapper
        )

    def get_by_email(self, email: str):

        stmt = select(UserModel).where(UserModel.email == email)
        result = self.session.execute(stmt)
        model = result.scalars().one_or_none()

        if not model:
            return None

        return self.mapper.to_entity(model)

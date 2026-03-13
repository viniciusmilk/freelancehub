from typing import Optional, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from .....domain.entities.users import User
from ..mappers import UserMapper
from ..models import UserModel
from .base_repository import BaseRepository

Entity = TypeVar('Entity')
Model = TypeVar('Model')


class UserRepository(BaseRepository[User, UserModel]):
    def __init__(self, session: Session):
        super().__init__(
            session=session, model_class=UserModel, mapper=UserMapper
        )

    def get_by_email(self, email: str) -> Optional[Entity]:

        stmt = select(self.model_class).where(self.model_class.email == email)
        result = self.session.execute(stmt)
        model = result.scalars().one_or_none()

        if not model:
            return None

        return self.mapper.to_entity(model)

    def update(self, user_data: Entity) -> Optional[Entity]:
        stmt = select(self.model_class).where(
            self.model_class.id == str(user_data.id)
        )
        result = self.session.execute(stmt)
        model = result.scalars().one_or_none()

        if not model:
            return None

        for key, value in user_data.__dict__.items():
            if hasattr(model, key) and key != 'id':
                setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)
        return self.mapper.to_entity(model)

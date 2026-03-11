from typing import Generic, List, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from ..mappers.base_mapper import BaseMapper

Entity = TypeVar('Entity')
Model = TypeVar('Model')


class BaseRepository(Generic[Entity, Model]):
    def __init__(
        self,
        session: Session,
        model_class: Type[Model],
        mapper: Type[BaseMapper],
    ):
        self.session = session
        self.model_class = model_class
        self.mapper = mapper

    def create(self, entity: Entity) -> Entity:

        model = self.mapper.to_model(entity)

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

        return self.mapper.to_entity(model)

    def get_by_id(self, id: str) -> Optional[Entity]:

        stmt = select(self.model_class).where(self.model_class.id == id)

        result = self.session.execute(stmt)
        model = result.scalars().one_or_none()

        if not model:
            return None

        return self.mapper.to_entity(model)

    def get_all(self) -> List[Entity]:

        stmt = select(self.model_class)
        result = self.session.execute(stmt)

        models = result.scalars().all()

        return [self.mapper.to_entity(model) for model in models]

    def delete(self, id: str):

        stmt = select(self.model_class).where(self.model_class.id == id)
        result = self.session.execute(stmt)

        model = result.scalars().one_or_none()

        if not model:
            raise ValueError(f'Entity with id {id} not found')

        self.session.delete(model)
        self.session.commit()

from typing import Generic, TypeVar

Entity = TypeVar('Entity')
Model = TypeVar('Model')


class BaseMapper(Generic[Entity, Model]):
    @staticmethod
    def to_entity(model: Model) -> Entity:
        raise NotImplementedError

    @staticmethod
    def to_model(entity: Entity) -> Model:
        raise NotImplementedError

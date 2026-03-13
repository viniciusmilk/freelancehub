from uuid import UUID

from .....domain.entities import Project
from ..models.project_model import ProjectModel
from .base_mapper import BaseMapper


class ProjectMapper(BaseMapper[Project, ProjectModel]):
    @staticmethod
    def to_entity(model: ProjectModel) -> Project:
        return Project(
            id=UUID(model.id),
            title=model.title,
            description=model.description,
            budget=model.budget,
            status=model.status,
            client_id=UUID(model.client_id),
            freelancer_id=UUID(model.freelancer_id),
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def to_model(entity: Project) -> ProjectModel:
        return ProjectModel(
            id=str(entity.id),
            title=entity.title,
            description=entity.description,
            budget=entity.budget,
            status=entity.status,
            client_id=str(entity.client_id),
            freelancer_id=str(entity.freelancer_id),
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

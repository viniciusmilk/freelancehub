from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from .....domain.entities import Project
from .....domain.enums import ProjectStatus
from ..mappers import ProjectMapper
from ..models import ProjectModel
from .base_repository import BaseRepository


class ProjectRepository(BaseRepository[Project, ProjectModel]):
    def __init__(self, session: Session):
        super().__init__(
            session=session,
            model_class=ProjectModel,
            mapper=ProjectMapper,
        )

    def get_by_freelancer(self, freelancer_id: str) -> List[Project]:
        stmt = select(self.model_class).where(
            self.model_class.freelancer_id == freelancer_id
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_by_client(self, client_id: str) -> List[Project]:
        stmt = select(self.model_class).where(
            self.model_class.client_id == client_id
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_by_status(
        self, status: ProjectStatus, freelancer_id: str
    ) -> List[Project]:
        stmt = select(self.model_class).where(
            self.model_class.status == status,
            self.model_class.freelancer_id == freelancer_id,
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_by_client_and_freelancer(
        self, client_id: str, freelancer_id: str
    ) -> List[Project]:
        stmt = select(self.model_class).where(
            self.model_class.client_id == client_id,
            self.model_class.freelancer_id == freelancer_id,
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def get_by_title(self, freelancer_id: str, title: str) -> List[Project]:
        stmt = select(self.model_class).where(
            self.model_class.title == title,
            self.model_class.freelancer_id == freelancer_id,
        )
        result = self.session.execute(stmt)
        models = result.scalars().all()

        if not models:
            return None

        return [self.mapper.to_entity(model) for model in models]

    def update(self, project_data: Project) -> Optional[Project]:
        stmt = select(self.model_class).where(
            self.model_class.id == str(project_data.id)
        )
        result = self.session.execute(stmt)
        model = result.scalars().one_or_none()

        if not model:
            return None

        for key, value in project_data.__dict__.items():
            if hasattr(model, key) and key != 'id':
                setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)

        return self.mapper.to_entity(model)

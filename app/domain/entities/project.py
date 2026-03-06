from pydantic import BaseModel

from app.domain.enums import ProjectStatus


class Project(BaseModel):
    id: int
    title: str
    description = str
    client_id: int
    freelancer_id = int
    status = ProjectStatus

    class Config:
        from_attributes = True

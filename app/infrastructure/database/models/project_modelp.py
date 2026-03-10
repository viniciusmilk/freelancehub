from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum

from app.infrastructure.database.base_model import BaseModel
from app.domain.enums import ProjectStatus

class ProjectModel(BaseModel):
    __tablename__ = 'projects'
    
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[ProjectStatus] = mapped_column(
        Enum(ProjectStatus, name='project_status'), nullable=False,
    )
    budget: Mapped[float] = mapped_column(Float, nullable=False)
    client_id: Mapped[str] = mapped_column(
        ForeignKey("clients.id"),
        nullable=False,
        index=True,
    )
    freelancer_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )
    
    client = relationship("ClientModel", back_populates="projects")
    freelancer = relationship("UserModel", back_populates="projects")
    contracts = relationship("ContractModel", back_populates="project", cascade="all, delete-orphan")
    
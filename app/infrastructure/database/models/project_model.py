#Project Model
from sqlalchemy import (
    Enum,
    Float,
    ForeignKey,
    String,
    CheckConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.domain.enums import ProjectStatus
from app.infrastructure.database.base_model import BaseModel


class ProjectModel(BaseModel):
    __tablename__ = 'projects'
    __table_args__ = (
        CheckConstraint('budget >= 0', name='check_budget_non_negative'),
    )

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[ProjectStatus] = mapped_column(
        Enum(ProjectStatus, name='project_status'), nullable=False,
    )
    budget: Mapped[float] = mapped_column(Float, nullable=False)
    client_id: Mapped[str] = mapped_column(
        ForeignKey("clients.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    freelancer_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    client = relationship("ClientModel", back_populates="projects")
    freelancer = relationship("UserModel", back_populates="projects")
    contracts = relationship(
        "ContractModel",
        back_populates="project",
        cascade="all, delete-orphan"
    )

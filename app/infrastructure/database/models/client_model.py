
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.infrastructure.database.base_model import BaseModel


class ClientModel(BaseModel):
    __tablename__ = 'clients'

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    owner_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    owner = relationship("UserModel", back_populates="clients")

    projects = relationship(
        "ProjectModel",
        back_populates="client",
        cascade="all, delete-orphan",
    )

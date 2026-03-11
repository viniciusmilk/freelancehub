#Client Model
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.infrastructure.database.base_model import BaseModel


class ClientModel(BaseModel):
    __tablename__ = 'clients'
    __table_args__ = (
        UniqueConstraint(
            "owner_id",
            "name",
            name="uq_client_owner_name"
        ),
    )
    
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    owner_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    owner = relationship("UserModel", back_populates="clients")

    projects = relationship(
        "ProjectModel",
        back_populates="client",
        cascade="all, delete-orphan",
    )

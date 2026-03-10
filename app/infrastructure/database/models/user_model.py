from typing import Optional

from sqlalchemy import Enum, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.domain.enums import UserRole
from app.infrastructure.database.base_model import BaseModel

# Import para forward reference
from .client_model import ClientModel


class UserModel(BaseModel):
    __tablename__ = 'users'
    username: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )
    first_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    password_hash: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name='user_role'),
        nullable=False,
    )
    oauth_provider: Mapped[Optional[str]] = mapped_column(
        String,
        nullable=True,
    )

    clients: Mapped[list["ClientModel"]] = relationship(
        "ClientModel",
        back_populates="owner",
        cascade="all, delete-orphan",
    )

    projects: Mapped[list["ProjectModel"]] = relationship(
        "ProjectModel",
        back_populates="freelancer",
        cascade="all, delete-orphan",
    )

from typing import Optional

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.enums import UserRole
from app.infrastructure.database.base_model import BaseModel


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

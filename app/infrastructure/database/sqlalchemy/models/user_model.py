# User Model
from typing import Optional

from sqlalchemy import (
    Enum,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.domain.enums import UserRole

from ..base_model import BaseModel

# Import para forward reference
from .client_model import ClientModel
from .contract_model import ContractModel
from .invoice_model import InvoiceModel
from .project_model import ProjectModel


class UserModel(BaseModel):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint('email', name='uq_email'),
        UniqueConstraint('username', name='uq_username'),
    )
    username: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )
    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(50),
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

    clients: Mapped[list['ClientModel']] = relationship(
        'ClientModel',
        back_populates='owner',
        cascade='all, delete-orphan',
    )

    projects: Mapped[list['ProjectModel']] = relationship(
        'ProjectModel',
        back_populates='freelancer',
        cascade='all, delete-orphan',
    )

    contracts: Mapped[list['ContractModel']] = relationship(
        'ContractModel',
        back_populates='freelancer',
        cascade='all, delete-orphan',
    )

    invoices: Mapped[list['InvoiceModel']] = relationship(
        'InvoiceModel',
        back_populates='freelancer',
        cascade='all, delete-orphan',
    )

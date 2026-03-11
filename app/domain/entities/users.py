from datetime import datetime
from typing import Optional
from uuid import UUID

from ..enums import UserRole

from .base_entity import BaseEntity


class User(BaseEntity):
    def __init__(
        self,
        id: UUID,
        username: str,
        email: str,
        first_name: str,
        last_name: str,
        password_hash: str,
        role: UserRole,
        created_at: datetime,
        updated_at: Optional[datetime] = None,
        oauth_provider: Optional[str] = None,
    ):
        super().__init__(id, created_at, updated_at)

        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = password_hash
        self.role = role
        self.oauth_provider = oauth_provider

        @property
        def full_name(self) -> str:
            return f"{self.first_name} {self.last_name}"

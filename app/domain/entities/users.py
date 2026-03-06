from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.domain.enums import UserRole


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    password_hash: str
    role: UserRole
    oauth_provider: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

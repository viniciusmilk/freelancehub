from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.domain.enums import UserRole


class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    password_hash: str
    role: UserRole
    oauth_provider: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

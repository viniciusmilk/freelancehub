from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.domain.enums import UserRole


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: UserRole

    model_config = {'from_attributes': True}


class UserResponseSchema(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    role: UserRole
    created_at: datetime
    updated_at: datetime

    model_config = {'from_attributes': True}


class UserListResponseSchema(BaseModel):
    users: list[UserResponseSchema]

    model_config = {'from_attributes': True}

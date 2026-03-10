from functools import lru_cache

from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.use_cases import (
    CreateUserUseCase,
    DeleteUserUseCase,
    GetUsersUseCase,
    GetUserUseCase,
)
from app.core.config import Settings
from app.infrastructure.database.repositories.user_repository import (
    UserRepository,
)
from app.infrastructure.database.session import SessionLocal


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_create_user_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
) -> CreateUserUseCase:
    return CreateUserUseCase(user_repository)


def get_get_users_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
) -> GetUsersUseCase:
    return GetUsersUseCase(user_repository)


def get_get_user_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
) -> GetUserUseCase:
    return GetUserUseCase(user_repository)


def get_delete_user_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
) -> DeleteUserUseCase:
    return DeleteUserUseCase(user_repository)


@lru_cache()
def get_settings() -> Settings:
    return Settings()

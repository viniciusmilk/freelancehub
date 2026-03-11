from fastapi import Depends
from sqlalchemy.orm import Session

from ..application.use_cases import CreateUserUseCase
from ..infrastructure.database.sqlalchemy.session import SessionLocal
from ..infrastructure.database.sqlalchemy.repositories import UserRepository


def get_db_session():
    with SessionLocal() as session:
        yield session


def get_user_repository(session: Session = Depends(get_db_session)):
    return UserRepository(session)


def get_create_user_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
):
    return CreateUserUseCase(user_repository)

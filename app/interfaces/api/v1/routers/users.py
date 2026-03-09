from http import HTTPStatus

from fastapi import APIRouter, Depends

from app.application.use_cases import CreateUserUseCase, GetUsersUseCase
from app.interfaces.dependencies import (
    get_create_user_use_case,
    get_get_users_use_case,
)
from app.interfaces.schemas import (
    UserCreateSchema,
    UserListResponseSchema,
    UserResponseSchema,
)

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    '/', response_model=UserResponseSchema, status_code=HTTPStatus.CREATED
)
def create_user(
    user_data: UserCreateSchema,
    create_user_use_case: CreateUserUseCase = Depends(
        get_create_user_use_case
    ),
):
    return create_user_use_case.execute(user_data)


@router.get(
    '/', response_model=UserListResponseSchema, status_code=HTTPStatus.OK
)
def get_users(
    get_users_use_case: GetUsersUseCase = Depends(get_get_users_use_case),
):
    users = get_users_use_case.execute()
    return {'users': users}

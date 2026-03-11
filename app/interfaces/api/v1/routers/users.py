from http import HTTPStatus

from fastapi import APIRouter, Depends

from .....application.use_cases import (
    CreateUserUseCase,
    DeleteUserUseCase,
    GetUsersUseCase,
    GetUserUseCase,
    UpdateUserUseCase,
)
from .....interfaces.dependencies import (
    get_create_user_use_case,
    get_delete_user_use_case,
    get_get_user_use_case,
    get_get_users_use_case,
    get_update_user_use_case,
)
from .....interfaces.schemas import (
    UserCreateSchema,
    UserListResponseSchema,
    UserResponseSchema,
    UserUpdateSchema,
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


@router.get(
    '/{user_id}',
    response_model=UserResponseSchema,
    status_code=HTTPStatus.OK,
)
def get_user(
    user_id: str,
    get_user_use_case: GetUserUseCase = Depends(get_get_user_use_case),
):
    user = get_user_use_case.execute(user_id)
    return user


@router.delete(
    '/{user_id}',
    status_code=HTTPStatus.NO_CONTENT,
)
def delete_user(
    user_id: str,
    delete_user_use_case: DeleteUserUseCase = Depends(
        get_delete_user_use_case
    ),
):
    delete_user_use_case.execute(user_id)
    return {'message': 'User deleted'}


@router.put(
    '/{user_id}',
    response_model=UserResponseSchema,
    status_code=HTTPStatus.OK,
)
def update_user(
    user_id: str,
    user_data: UserUpdateSchema,
    update_user_use_case: UpdateUserUseCase = Depends(
        get_update_user_use_case
    ),
):
    data = user_data.model_dump(exclude_unset=True)
    user = update_user_use_case.execute(user_id, data)
    return user


@router.patch(
    '/{user_id}',
    response_model=UserResponseSchema,
    status_code=HTTPStatus.OK,
)
def patch_user(
    user_id: str,
    user_data: UserUpdateSchema,
    update_user_use_case: UpdateUserUseCase = Depends(
        get_update_user_use_case
    ),
):
    data = user_data.model_dump(exclude_unset=True)
    user = update_user_use_case.execute(user_id, data)
    return user

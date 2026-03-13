from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter(prefix='/clients', tags=['clients'])


@router.get('', status_code=HTTPStatus.OK)
def get_clients():
    return {'message': 'Hello, World!'}

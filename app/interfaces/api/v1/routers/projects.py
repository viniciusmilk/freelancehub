from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter(prefix='/projects', tags=['projects'])


@router.get('', status_code=HTTPStatus.OK)
def get_projects():
    return {'message': 'Hello, World!'}

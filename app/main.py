from fastapi import FastAPI

from app.interfaces.api.v1.api import api_router

app = FastAPI(title='FreelanceHub API')

app.include_router(api_router, prefix='/api/v1')


@app.get('/', status_code=200)
def root():
    return {'status': 'ok'}

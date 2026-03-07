from fastapi import FastAPI

from app.interfaces.api.v1.routers import users_router

app = FastAPI(title='FreelanceHub API')

app.include_router(users_router)


@app.get('/', status_code=200)
def root():
    return {'status': 'ok'}

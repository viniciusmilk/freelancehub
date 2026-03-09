from fastapi import APIRouter

from .routers import users_router

api_router = APIRouter()
api_router.include_router(users_router)

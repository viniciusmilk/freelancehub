from fastapi import APIRouter

from .routers import clients_router, projects_router, users_router

api_router = APIRouter()
api_router.include_router(users_router)
api_router.include_router(clients_router)
api_router.include_router(projects_router)

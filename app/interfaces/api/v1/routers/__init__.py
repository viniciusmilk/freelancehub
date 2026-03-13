from .clients import router as clients_router
from .projects import router as projects_router
from .users import router as users_router

__all__ = [
    'users_router',
    'clients_router',
    'projects_router',
]

from fastapi import APIRouter

from app.api.v1.routers import auth_router, users_router

api_router = APIRouter(prefix="/v1")
api_router.include_router(auth_router.router)
api_router.include_router(users_router.router)

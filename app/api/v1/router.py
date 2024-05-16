from fastapi import APIRouter

from app.api.v1.routes import sample

api_router = APIRouter(prefix="/V1")
api_router.include_router(sample.router)

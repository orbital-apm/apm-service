from dotenv import load_dotenv
from fastapi import FastAPI

from app.api.v1.router import api_router
from app.api import auth_router, build_router

load_dotenv()

app = FastAPI()
app.include_router(api_router)
app.include_router(auth_router.router)
app.include_router(build_router.router)

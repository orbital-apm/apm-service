from fastapi import FastAPI
from app.api.v1.router import api_router
from app.api import authentication

app = FastAPI()
app.include_router(api_router)
app.include_router(authentication.router)

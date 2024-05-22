from fastapi import FastAPI
from pydantic import BaseModel
from typing import *
from app.api.v1.router import api_router

app = FastAPI()
app.include_router(api_router)

# User authentication endpoint




# Tutorials and Guides endpoint



from fastapi import FastAPI
from pydantic import BaseModel
from typing import *
from app.api.v1.router import api_router

app = FastAPI()
app.include_router(api_router)

# User authentication endpoint




# Tutorials and Guides endpoint

class Tutorial(BaseModel):
    id: int
    title: str
    content: str
    category: str
    created: str
    updated: Optional[str] = None

class Guide(BaseModel):
    id: int
    title: str
    content: str
    category: str
    created: str
    updated: Optional[str] = None


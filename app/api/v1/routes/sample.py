from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def sample():
    return {"Hello": "World"}

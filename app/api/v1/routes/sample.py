from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def sample() -> dict[str, str]:
    return {"Hello": "World"}

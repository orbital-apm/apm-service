from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.api.v1.routers import auth_router, parts_router, builds_router, marketplace_router

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router)
app.include_router(auth_router.router)
app.include_router(parts_router.router)
app.include_router(builds_router.router)
app.include_router(parts_router.router)
app.include_router(marketplace_router.router)


@app.get("/ping")
async def ping() -> JSONResponse:
    return JSONResponse(content={"Message": "Successful ping"}, status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)
